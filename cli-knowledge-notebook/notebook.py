import pymysql
from config import DB_CONFIG
from datetime import datetime


def get_conn():
    return pymysql.connect(**DB_CONFIG)


def add_note():
    title = input("标题：")
    content = input("内容：")

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (%s, %s)",
        (title, content)
    )
    conn.commit()
    conn.close()
    print(f"✅ 笔记「{title}」已保存")


def list_notes():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, created_at FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 还没有笔记")
        return

    for row in rows:
        print(f"[{row[0]}] {row[1]} | {row[2]}")


def main():
    print("=== 个人知识库 ===")
    print("1. 添加笔记")
    print("2. 列出笔记")
    print("0. 退出")

    choice = input("选择：")

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "0":
        print("拜拜")
        return
    else:
        print("无效选择")


if __name__ == "__main__":
    main()
