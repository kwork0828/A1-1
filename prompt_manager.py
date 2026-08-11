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


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 번호입니다. 메뉴에 있는 번호를 입력해 주세요.")


if __name__ == "__main__":
    main()



