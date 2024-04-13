import re
from datetime import datetime
from dateutil.parser import parse


def parse_exam_data(line, default_year=datetime.now().year):
    """ 解析不同格式的考试信息，返回考试开始时间和原始行内容的元组 """
    # 尝试匹配多种日期格式
    datetime_patterns = [
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
        r'\d{4}年-\d{2}月-\d{2}日-\d{2}时',
        r'\d{4}.\d{2}.\d{2} \d{2}:\d{2}:\d{2}',
        r'\d{2}月\d{2}日\d{2}:\d{2}',
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}',
        r'\d{4}.\d{2}.\d{2} \d{2}:\d{2}',
        r'\d{2}.\d{2} \d{2}:\d{2}',
        r'(\d{4})(\d{2})(\d{2})'
    ]

    for pattern in datetime_patterns:
        match = re.search(pattern, line)
        if match:
            try:
                if pattern == r'(\d{4})(\d{2})(\d{2})':  # 特殊处理年份省略的情况
                    date_str = f"{default_year}-{match.group(2)}-{match.group(3)} 00:00:00"
                    start_time = parse(date_str)
                else:
                    start_time = parse(match.group())
                return start_time, line
            except ValueError:
                continue
    return None, line


def read_and_sort_exams(filename):
    """ 读取和排序考试数据文件 """
    with open(filename, 'r', encoding='utf-8') as file:
        exams = [parse_exam_data(line) for line in file if line.strip()]
        exams = [exam for exam in exams if exam[0] is not None]
        exams.sort()
    return [exam[1] for exam in exams]


def write_sorted_exams(filename, sorted_exams):
    """ 将排序后的考试信息写回文件 """
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(sorted_exams)


# 示例用法：
filename = 'exam_data.txt'

# 读取和排序考试信息
sorted_exams = read_and_sort_exams(filename)

# 写回排序后的考试信息到文件
write_sorted_exams(filename, sorted_exams)
