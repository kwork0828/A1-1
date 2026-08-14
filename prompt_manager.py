# prompt_manager.py
# 나만의 프롬프트 관리 프로그램

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "브랜드 광고 카피 작성",
        "content": "당신은 15년 경력의 카피라이터입니다. 사회적기업 브랜드의 10초 광고에 쓸 "
                   "한 문장 핵심 메시지를 3개 제안해 주세요.",
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "동화풍 캐릭터 키비주얼 생성",
        "content": "수채화 동화 일러스트 스타일, 파스텔 톤, 보라색 아기 코끼리 캐릭터, "
                   "밝고 따뜻한 조명, 텍스트와 로고 없음.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "10초 브랜드 광고 스토리보드",
        "content": "3개 장면으로 구성된 10초 광고 스토리보드를 만들어 주세요. "
                   "장면별 길이, 화면 구성, 나레이션을 표로 정리해 주세요.",
        "category": "영상 생성",
        "favorite": False,
    },
    {
        "title": "메일 자동 분류 규칙 설계",
        "content": "받은 메일 제목과 본문을 읽고 문의/견적/스팸 3가지로 분류한 뒤 "
                   "JSON 형식으로 출력해 주세요.",
        "category": "자동화",
        "favorite": False,
    },
]


def print_line():
    print("-" * 40)


def print_prompt_line(no, prompt):
    mark = " ⭐" if prompt["favorite"] else ""
    print(f"{no}. [{prompt['category']}] {prompt['title']}{mark}")


def input_nonempty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("입력값이 비어 있습니다. 다시 입력해 주세요.")


def choose_category():
    print("\n카테고리 선택:")
    for i, name in enumerate(CATEGORIES, 1):
        print(f"{i}) {name}")
    print("0) 직접 입력")
    choice = input("선택: ").strip()
    if choice == "0":
        return input_nonempty("카테고리 직접 입력: ")
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        return CATEGORIES[int(choice) - 1]
    print("잘못된 선택입니다. '기타'로 지정합니다.")
    return "기타"


def select_index(label="번호 입력: "):
    value = input(label).strip()
    if not value.isdigit():
        print("숫자를 입력해 주세요.")
        return -1
    number = int(value)
    if number < 1 or number > len(prompts):
        print("존재하지 않는 번호입니다.")
        return -1
    return number - 1


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_nonempty("제목: ")
    content = input_nonempty("내용: ")
    category = choose_category()
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("\n프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(prompts, 1):
        print_prompt_line(i, prompt)
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    category = choose_category()
    found = [p for p in prompts if p["category"] == category]
    if not found:
        print(f"\n'{category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트")
    for i, prompt in enumerate(found, 1):
        print_prompt_line(i, prompt)
    print(f"\n총 {len(found)}개")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input_nonempty("검색어: ").lower()
    found = [p for p in prompts
             if keyword in p["title"].lower() or keyword in p["content"].lower()]
    if not found:
        print(f"\n'{keyword}' 검색 결과가 없습니다.")
        return
    for i, prompt in enumerate(found, 1):
        print_prompt_line(i, prompt)
    print(f"\n검색 결과 {len(found)}개")


def show_detail():
    show_list()
    if not prompts:
        return
    index = select_index("\n상세히 볼 번호: ")
    if index == -1:
        return
    prompt = prompts[index]
    print_line()
    print(f"제목    : {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
    print(f"내용    : {prompt['content']}")
    print_line()


def toggle_favorite():
    show_list()
    if not prompts:
        return
    index = select_index("\n즐겨찾기 변경할 번호: ")
    if index == -1:
        return
    prompts[index]["favorite"] = not prompts[index]["favorite"]
    state = "등록" if prompts[index]["favorite"] else "해제"
    print(f"\n'{prompts[index]['title']}' 즐겨찾기를 {state}했습니다.")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    found = [p for p in prompts if p["favorite"]]
    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(found, 1):
        print_prompt_line(i, prompt)
    print(f"\n총 {len(found)}개")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 번호입니다. 메뉴에 있는 번호를 입력해 주세요.")


if __name__ == "__main__":
    main()
