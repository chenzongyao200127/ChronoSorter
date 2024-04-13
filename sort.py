import re
from datetime import datetime
from dateutil.parser import parse


def parse_exam_data(line, default_year=datetime.now().year):
    """解析不同格式的考试信息，返回考试开始时间和原始行内容的元组。"""
    datetime_patterns = [
        r'(\d{4})年[-/](\d{2})月[-/](\d{2})日[-/](\d{2})时',
        r'(\d{4})[-/.](\d{2})[-/.](\d{2})[ T](\d{2}):(\d{2})',
        r'(\d{4})[-/.](\d{2})[-/.](\d{2})',
        r'(\d{2})[-/.](\d{2})',
        r'(\d{1,2}):(\d{2}) (AM|PM) (\d{1,2})[-/.](\d{2})[-/.](\d{4})',
        r'(\d{2})(\d{2})',
        r'(\d{4})(\d{2})(\d{2})'  # YYYYMMDD格式
    ]

    # 预编译正则表达式以提高性能
    compiled_patterns = [re.compile(pattern) for pattern in datetime_patterns]

    for pattern in compiled_patterns:
        match = pattern.search(line)
        if match:
            groups = match.groups()
            try:
                date_str = construct_date_str(groups, pattern, default_year)
                start_time = parse(date_str)
                formatted_date = start_time.strftime('%Y-%m-%d %H:%M:%S')
                revised_line = f"{formatted_date} {line.strip()}\n"
                return start_time, revised_line
            except (ValueError, IndexError):
                continue  # 在解析失败时继续尝试其他格式
    return None, line


def construct_date_str(groups, pattern, default_year):
    """根据捕获的组和正则表达式构建日期字符串。"""
    if '年' in pattern.pattern or any(x in pattern.pattern for x in ['/', '-', '.']):
        hour = groups[3] if len(groups) > 3 else '00'
        return f"{groups[0]}-{groups[1]}-{groups[2]} {hour}:00:00"
    elif 'AM' in pattern.pattern or 'PM' in pattern.pattern:
        return f"{groups[5]}-{groups[3]}-{groups[4]} {groups[0]}:{groups[1]} {groups[2]}"
    elif len(groups) == 2:
        return f"{default_year}-{groups[0]}-{groups[1]} 00:00:00"
    elif len(groups) == 3:
        return f"{groups[0]}-{groups[1]}-{groups[2]} 00:00:00"
    return groups[0]


def read_and_sort_exams(filename):
    """ 读取和排序考试数据文件 """
    with open(filename, 'r', encoding='utf-8') as file:
        exams = [parse_exam_data(line) for line in file if line.strip()]
        exams = [exam for exam in exams if exam[0] is not None]
        exams.sort(key=lambda x: x[0])  # 根据日期排序
    return [exam[1] for exam in exams]


def write_sorted_exams(filename, sorted_exams):
    """ 将排序后的考试信息写回文件 """
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(sorted_exams)


# 示例用法：
source_filename = 'ori_exam_data.txt'
filename = 'exam_data.txt'

# 读取和排序考试信息
sorted_exams = read_and_sort_exams(source_filename)

# 写回排序后的考试信息到文件
write_sorted_exams(filename, sorted_exams)
