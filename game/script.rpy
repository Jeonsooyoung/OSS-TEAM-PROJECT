# 이 파일에 게임 스크립트를 입력합니다.



# 게임에서 사용할 캐릭터를 정의합니다.
init -1 python:
    class Character_info:
        def __init__(self, name, image, personality, description, color):
            self.name = name
            self.image = image
            self.personality = personality
            self.description = description
            self.color = color
            self.character = Character(name, color=color)
            renpy.image(name, image)
        
        # def get_info(self):
        #     return f"{self.name}는 {self.personality}이고, {self.description}"
    
    # 캐릭터 인스턴스 생성
    chanmi = Character_info("찬미", "images/character/chanmi.jpg", "똑 부러지며 리더십이 강한 성격", "학생회에서 활동하며, 학과 행사와 활동에 적극적이다. 철저하게 자기관리를 하며 공부와 활동 모두 열심히 한다.", "#9A2EFE")
    ari = Character_info("아리", "images/character/ari.jpg", "사교성이 부족하며 배려심이 깊고 차분한 성격", "다소 내성적이지만 컴퓨터 공학에 큰 열정을 가지고 있으며 성실하게 수업에 임하는 학생이다.", "#25418d")
    sena = Character_info("세나", "images/character/sena.jpg", "활발하고 사교적인 성격", "주변에 늘 친구가 많으며, 인기가 많아 학과의 분위기 메이커 역할을 한다. 학업보다는 학과 활동이나 교내 축제에 관심이 많다.", "#FF8000")
    all_characters = [chanmi, ari, sena]

    # Character 객체 정의
    c = chanmi.character
    a = ari.character
    s = sena.character


# 여기에서부터 게임이 시작합니다.
label start:

    transform vertical:
        yalign 0.5    # 이미지의 y축 위치를 미리 지정
    
    transform left:
        xalign 0.15
    transform right:
        xalign 0.85   #left랑 right의 기본값이 너무 끝에 있는 것 같아서 좀 가운데로 당김

    "안녕하세요, 게임을 시작하기전 당신의 이름을 알려주세요!"

    $ name_entered = False

    # 이름 입력 루프
    while not name_entered:
        $ player_name = renpy.input("당신의 이름을 입력해주세요.")

        if player_name:  # 이름이 입력되었으면
            $ name_entered = True
        else:  # 이름이 비어 있으면 메시지 출력
            "이름을 입력해주세요."

    # 이름 확인 및 스토리 진행
    "당신의 이름은 [player_name]이군요! 게임을 시작합니다!"
    
    show chanmi at center, vertical
    c "안녕하세요, 저는 찬미입니다."

    show ari at left, vertical  # 아리의 이미지를 왼쪽에 표시합니다
    a "안녕하세요..."

    show sena at right, vertical  # 세나의 이미지를 오른쪽에 표시합니다
    s "모두 안녕!"

    return
