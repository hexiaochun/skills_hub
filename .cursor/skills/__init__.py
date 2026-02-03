"""
V3 Skills 管理模块

Skills 是预定义的模型使用指南，帮助 AI 理解如何正确调用模型。
每个 Skill 对应一个或多个模型，包含：
- 模型介绍
- 参数说明
- 调用示例
- 最佳实践

目录结构（两级）：
skills/
├── sora-2/
│   └── SKILL.md
├── flux2-flash/
│   └── SKILL.md
└── ...
"""

import re
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


# Skills 根目录
SKILLS_DIR = Path(__file__).parent


# ========== 模型-Skill 映射 ==========
# 一个模型可以对应多个 Skills，一个 Skill 也可以对应多个模型

MODEL_SKILL_MAPPING: Dict[str, List[str]] = {
    # Sora 2 系列 -> [sora-2] 或 [sora-2, 其他skill]
    "fal-ai/sora-2/text-to-video": ["sora-2"],
    "fal-ai/sora-2/image-to-video": ["sora-2"],
    "fal-ai/sora-2/text-to-video/pro": ["sora-2"],
    "fal-ai/sora-2/image-to-video/pro": ["sora-2"],
    "fal-ai/sora-2/video-to-video/remix": ["sora-2"],
    
    # Wan 系列
    "wan/v2.6/text-to-video": ["wan-video"],
    "wan/v2.6/image-to-video": ["wan-video"],
    "wan/v2.6/image-to-video/flash": ["wan-video"],
    "wan/v2.6/reference-to-video": ["wan-video"],
    
    # Flux 2 Flash
    "fal-ai/flux-2/flash": ["flux2-flash"],
    
    # Seedream 系列
    "fal-ai/bytedance/seedream/v4.5/text-to-image": ["seedream-image"],
    "fal-ai/bytedance/seedream/v4.5/edit": ["seedream-image"],
    
    # Nano Banana Pro
    "fal-ai/nano-banana-pro": ["nano-banana-pro", "nano-pro-shuihu"],
    
    # Kling Motion Control
    "fal-ai/kling-video/v2.6/standard/motion-control": ["kling-motion-control"],
    
    # Minimax（海螺）音频系列
    "minimax/t2a": ["minimax-audio"],
    "minimax/voice-design": ["minimax-audio"],
    "minimax/voice-clone": ["minimax-audio"],
    "minimax/music-gen": ["minimax-audio"],
    
    # 示例：一个模型对应多个 Skills
    # "fal-ai/some-model": ["skill-1", "skill-2", "skill-3"],
}


def get_skills_for_model(model_id: str) -> List[str]:
    """获取模型对应的所有 Skill ID 列表"""
    return MODEL_SKILL_MAPPING.get(model_id, [])


def get_skill_for_model(model_id: str) -> Optional[str]:
    """获取模型对应的主要 Skill ID（第一个）- 向后兼容"""
    skills = MODEL_SKILL_MAPPING.get(model_id, [])
    return skills[0] if skills else None


def get_models_for_skill(skill_id: str) -> List[str]:
    """获取 Skill 对应的所有模型 ID"""
    return [
        model_id 
        for model_id, skill_ids in MODEL_SKILL_MAPPING.items() 
        if skill_id in skill_ids
    ]


def _parse_frontmatter(content: str) -> Dict[str, Any]:
    """
    解析 SKILL.md 的 YAML frontmatter
    
    Returns:
        {
            "name": str,
            "description": str,
            "category": str,      # image/video/audio/tool/multimodal
            "tags": [str],
            "featured": bool
        }
    """
    result = {
        "name": None,
        "description": None,
        "category": None,
        "tags": [],
        "featured": False
    }
    
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        
        # 解析各字段
        name_match = re.search(r'name:\s*(.+)', frontmatter)
        if name_match:
            result["name"] = name_match.group(1).strip()
        
        desc_match = re.search(r'description:\s*(.+)', frontmatter)
        if desc_match:
            result["description"] = desc_match.group(1).strip()
        
        category_match = re.search(r'category:\s*(.+)', frontmatter)
        if category_match:
            result["category"] = category_match.group(1).strip()
        
        # 解析 tags（支持 YAML 列表格式）
        tags_match = re.search(r'tags:\s*\[([^\]]*)\]', frontmatter)
        if tags_match:
            tags_str = tags_match.group(1)
            result["tags"] = [t.strip().strip('"\'') for t in tags_str.split(',') if t.strip()]
        else:
            # 尝试解析多行 YAML 列表格式
            tags_lines = re.findall(r'tags:\s*\n((?:\s*-\s*.+\n?)+)', frontmatter)
            if tags_lines:
                result["tags"] = [
                    line.strip().lstrip('- ').strip('"\'')
                    for line in tags_lines[0].split('\n')
                    if line.strip().startswith('-')
                ]
        
        featured_match = re.search(r'featured:\s*(true|yes|1)', frontmatter, re.IGNORECASE)
        if featured_match:
            result["featured"] = True
    
    return result


def get_skill_info(skill_id: str) -> Optional[Dict[str, Any]]:
    """
    获取 Skill 的详细信息
    
    Returns:
        {
            "id": str,
            "name": str,
            "description": str,
            "category": str,
            "tags": [str],
            "featured": bool,
            "content": str,   # SKILL.md 内容
            "files": [{"path": str, "size": int}],
            "related_models": [str]
        }
    """
    skill_dir = SKILLS_DIR / skill_id
    if not skill_dir.exists() or not skill_dir.is_dir():
        return None
    
    # 读取 SKILL.md
    skill_md = skill_dir / "SKILL.md"
    content = skill_md.read_text(encoding='utf-8') if skill_md.exists() else ""
    
    # 解析 frontmatter
    meta = _parse_frontmatter(content)
    
    # 获取文件列表
    files = []
    for file_path in skill_dir.rglob('*'):
        if file_path.is_file():
            rel_path = str(file_path.relative_to(skill_dir))
            files.append({
                "path": rel_path,
                "size": file_path.stat().st_size
            })
    
    return {
        "id": skill_id,
        "name": meta["name"] or skill_id,
        "description": meta["description"] or "",
        "category": meta["category"],
        "tags": meta["tags"],
        "featured": meta["featured"],
        "content": content,
        "files": files,
        "related_models": get_models_for_skill(skill_id)
    }


def list_all_skills(
    category: Optional[str] = None,
    tag: Optional[str] = None,
    keyword: Optional[str] = None,
    featured_only: bool = False,
    sort_by: str = "name",
    limit: Optional[int] = None,
    offset: int = 0
) -> Tuple[List[Dict[str, Any]], int]:
    """
    列出所有可用的 Skills，支持筛选、搜索、分页
    
    Args:
        category: 分类筛选（image/video/audio/tool）
        tag: 标签筛选
        keyword: 关键词搜索（搜索 name 和 description）
        featured_only: 只返回推荐的 Skills
        sort_by: 排序字段（name/category）
        limit: 每页数量，None 表示不分页
        offset: 偏移量
    
    Returns:
        (skills_list, total_count)
    """
    all_skills = []
    
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        # 跳过非目录、隐藏文件、__pycache__ 等
        if not skill_dir.is_dir():
            continue
        if skill_dir.name.startswith('.') or skill_dir.name.startswith('__'):
            continue
        
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        
        content = skill_md.read_text(encoding='utf-8')
        meta = _parse_frontmatter(content)
        
        # 统计文件数量
        file_count = sum(1 for _ in skill_dir.rglob('*') if _.is_file())
        
        all_skills.append({
            "id": skill_dir.name,
            "name": meta["name"] or skill_dir.name,
            "description": meta["description"] or "",
            "category": meta["category"],
            "tags": meta["tags"],
            "featured": meta["featured"],
            "file_count": file_count,
            "related_models": get_models_for_skill(skill_dir.name)
        })
    
    # ========== 筛选 ==========
    filtered_skills = all_skills
    
    # 分类筛选
    if category:
        filtered_skills = [s for s in filtered_skills if s.get("category") == category]
    
    # 标签筛选
    if tag:
        filtered_skills = [s for s in filtered_skills if tag in s.get("tags", [])]
    
    # 关键词搜索
    if keyword:
        keyword_lower = keyword.lower()
        filtered_skills = [
            s for s in filtered_skills
            if keyword_lower in s["name"].lower()
            or keyword_lower in s.get("description", "").lower()
            or keyword_lower in s["id"].lower()
        ]
    
    # 只返回推荐
    if featured_only:
        filtered_skills = [s for s in filtered_skills if s.get("featured")]
    
    # ========== 排序 ==========
    if sort_by == "name":
        filtered_skills.sort(key=lambda x: x.get("name", ""))
    elif sort_by == "category":
        filtered_skills.sort(key=lambda x: (x.get("category") or "zzz", x.get("name", "")))
    elif sort_by == "featured":
        # 推荐的排在前面
        filtered_skills.sort(key=lambda x: (0 if x.get("featured") else 1, x.get("name", "")))
    
    # 记录总数
    total_count = len(filtered_skills)
    
    # ========== 分页 ==========
    if limit is not None:
        filtered_skills = filtered_skills[offset:offset + limit]
    
    return filtered_skills, total_count


def list_all_skills_simple() -> List[Dict[str, Any]]:
    """
    列出所有 Skills（简单版本，向后兼容）
    
    Returns:
        [{
            "id": str,
            "name": str,
            "description": str,
            "category": str,
            "tags": [str],
            "featured": bool,
            "file_count": int,
            "related_models": [str]
        }]
    """
    skills, _ = list_all_skills()
    return skills


def create_skill_zip(skill_id: str) -> Optional[BytesIO]:
    """
    创建单个 Skill 的 ZIP 压缩包
    
    Returns:
        BytesIO 对象，包含 ZIP 内容；如果 Skill 不存在则返回 None
    """
    skill_dir = SKILLS_DIR / skill_id
    if not skill_dir.exists() or not skill_dir.is_dir():
        return None
    
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_dir.rglob('*'):
            if file_path.is_file():
                # 相对路径: skill_id/xxx
                arcname = f"{skill_id}/{file_path.relative_to(skill_dir)}"
                zf.write(file_path, arcname)
    
    zip_buffer.seek(0)
    return zip_buffer


def create_all_skills_zip() -> BytesIO:
    """
    创建所有 Skills 的 ZIP 压缩包
    
    Returns:
        BytesIO 对象，包含所有 Skills
    """
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for skill_dir in SKILLS_DIR.iterdir():
            # 跳过非目录、隐藏文件、__pycache__ 等
            if not skill_dir.is_dir():
                continue
            if skill_dir.name.startswith('.') or skill_dir.name.startswith('__'):
                continue
            
            for file_path in skill_dir.rglob('*'):
                if file_path.is_file():
                    arcname = f"{skill_dir.name}/{file_path.relative_to(skill_dir)}"
                    zf.write(file_path, arcname)
    
    zip_buffer.seek(0)
    return zip_buffer
