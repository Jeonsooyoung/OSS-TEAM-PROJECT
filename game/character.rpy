# character.rpy

init -2 python:
    class Character_info:
        def __init__(self, name, image, personality, description, color):
            self.name = name
            self.image = image
            self.personality = personality
            self.description = description
            self.color = color
            self.character = Character(name, color=color)
            self.affection = 0
            renpy.image(name, image)
        
        def increase_affection(self, amount):
            self.affection += amount
            if self.affection > 100:
                self.affection = 100
        
        def decrease_affection(self, amount):
            self.affection -= amount
            if self.affection < 0:
                self.affection = 0
        
        def get_affection(self):
            return self.affection

    # 캐릭터 인스턴스 생성
    chanmi = Character_info("찬미", "images/character/chanmi.jpg", "똑 부러지며 리더십이 강한 성격", "학생회에서 활동하며, 학과 행사와 활동에 적극적이다. 철저하게 자기관리를 하며 공부와 활동 모두 열심히 한다.", "#9A2EFE")
    ari = Character_info("아리", "images/character/ari.jpg", "사교성이 부족하며 배려심이 깊고 차분한 성격", "다소 내성적이지만 컴퓨터 공학에 큰 열정을 가지고 있으며 성실하게 수업에 임하는 학생이다.", "#25418d")
    sena = Character_info("세나", "images/character/sena.jpg", "활발하고 사교적인 성격", "주변에 늘 친구가 많으며, 인기가 많아 학과의 분위기 메이커 역할을 한다. 학업보다는 학과 활동이나 교내 축제에 관심이 많다.", "#FF8000")
    all_characters = [chanmi, ari, sena]

    # Character 객체 정의
    c = chanmi.character
    a = ari.character
    s = sena.character

# 호감도 표시 함수
init python:
    def show_affection(character):
        renpy.say(None, f"{character.name}의 현재 호감도: {character.get_affection()}")