define p = Character(" ")
# define s1 = Character("학생 1")
# define s2 = Character("학생 2")
# define s3 = Character("학생 3")
image bg_beach_day = "background/bg_beach_day.jpg"
image bg_bbq_evening = "background/bbq_evening.jpg"
image bg_drinking_game = "background/drinking.jpg"
image bg_beach_evening = "background/beach_evening.jpg"
label chapter2:

    $ load_game_state()
    $ sync_player_name()

    scene bg_beach_day
    with dissolve

    p "새 학기가 시작된 지도 어느덧 한 달. 설렘 가득한 마음으로 컴퓨터공학과 학생들은 MT를 떠나 대천해수욕장에 도착했다."
    p "버스에서 내리자마자, 다들 설렘이 가득한 얼굴로 짐을 정리하고는 하나둘 해수욕장으로 모여들었다."
    p "반짝이는 바다와 시원한 바람이 불고, 모두가 들뜬 목소리로 여기저기서 이야기꽃을 피운다." 

    # 남자 주인공의 독백
    "[player_name]" "바다는 참 오랜만이네. 고등학교 때 수학여행 이후 처음인가."
    "[player_name]" "대학 생활이라... 아직도 실감이 잘 안 나. 이렇게 떠들썩한 분위기 속에 내가 어울릴 수 있을까?"

    # 해수욕장에서의 상황
    s "야, [player_name] 뭐해? 너만 안 와서 다들 기다리고 있잖아! 빨리 와!"
    "[player_name]" "(역시 세나누나는 여기서도 활발하네..ㅎㅎ)"
    "[player_name]" "알았어. 금방 갈게!"
    p "그렇게 모두가 해수욕장에 모이고, 곧바로 조별로 나누어 게임을 시작했다."
    p "게임은 팀워크를 시험하는 다양한 미션들로 구성되어 있었다. 동기들과 웃고 떠들며 협력하는 모습은 이미 분위기를 한층 뜨겁게 만들었다."
    p "각 조가 경쟁을 벌이면서도, 모두가 즐기고 있다는 것이 느껴졌다."

    p "게임이 한창 진행되던 중, 세나가 [player_name]에게 다가와 말을 걸었다."
    show sena at left with dissolve
    s "야, [player_name]! 다음 게임이 신발 던지기인데 너가 한 번 도전해볼래?"

    menu:
        s "야, [player_name]! 다음 게임이 신발 던지기인데 너가 한 번 도전해볼래?{fast}"
        "내 활약 보고 반해버려도 책임 못 진다?":
            "[player_name]" "훗 드디어 내가 나서야 되나?"
            "[player_name]" "제가 오송고의 신발 던지기 전설이였죠(후후)"
            $ sena.increase_affection(1) # 호감도 상승
            show sena_happy at left with dissolve
            s "ㅋㅋㅋㅋㅋ알겠어, 그럼 부탁한다! 우리 팀의 희망은 너야!"
            s "(보기보다 허세가 많네ㅎㅎ)"
            p "[player_name]는 자신감을 내비치며 게임에 도전했다."
            p "주변의 시선이 [player_name]에게 집중되자, 살짝 긴장되는 기운이 감돌았다."
            "[player_name]" "(좋아, 분위기는 내가 다 가져가는 거야. 다들 놀랄 준비는 됐겠지?)"
            "[player_name]" "(신이시여 저에게 힘을 주소서..!)"
            p "게임이 시작되고, [player_name]는 침착하게 미션을 수행하기 시작했다" 
            p "결과는 대성공! 팀원들은 환호했고, [player_name]도 자신감을 얻었다."
            s "우와! 진짜 잘하는데? 농담인 줄 알았더니 우리 팀 MVP가 여기 있었네!"
            "[player_name]" "흠, 이 정도는 기본이죠. 저 왕년에 진짜 잘했다니까요!"
            p "주변에서 터져 나오는 박수와 환호 소리에 [player_name]는 살짝 뿌듯한 표정을 지었다."

        "ㅈㄴ 하기 싫은데 어떻게 하지;;":
            "[player_name]" "음… 누나가 더 잘할 것 같은데요? 제가 하면 팀 점수가 위험할 수도 있으니까..ㅎㅎ"
            s "야, 설마 나한테 미루는 거야? 한 번 보여줘봐!!"
            "[player_name]" "(아니 하기 싫다는데 왜 자꾸 시킬려고 하는거야)"
            "[player_name]" "(좋게 좋게 넘어가보자)"
            "[player_name]" "아니, 그런 건 아니고... 누나가 워낙 잘할 것 같아서 그러죠ㅎ~ 저희 팀 에이스는 누나 아니겠어요?"
            show sena_sad at left with dissolve
            $ sena.decrease_affection(1)
            s "(우리 팀을 위해 한 번쯤 멋지게 나서주는 것도 괜찮았을 텐데... 조금 아쉽네)"
            hide sena_sad with dissolve
            show sena at left with dissolve
            s "치, 쫄보네. 그래, 이 누나가 한 수 보여줄게!"
            p "세나가 자신만만한 표정으로 앞으로 나서자, 팀원들 사이에서 환호와 응원이 쏟아졌다."
            "[player_name]" "누나, 믿어볼게요! 제대로 보여주세요!"
            p "게임이 시작되자, 세나는 평생 신발만 던져본 것처럼 자신의 신발을 날리기 시작했다."
            p "[player_name]는 안도의 한숨을 쉬며 뒤에서 그 모습을 지켜보았다."
            p "세나가 멋지게 미션을 성공시키자, 모두들 박수를 보냈다."
            "[player_name]" "(누나가 잘 해줘서 다행이다)"

    p "각 조가 경쟁을 벌이면서도, 모두가 게임을 즐겼다."
    p "점점 해가 기울어가며 바다는 황금빛으로 물들었고, 모든 팀원들은 숙소로 돌아갔다."
        
    scene bg_bbq_evening
    with fade

    # 바베큐에서의 상황
    p "저녁 시간이 다가오자, 바비큐 준비가 시작되었다."
    p "찬미가 상추, 수저, 포크 같은 것들을 정리하고 있는 모습이 보인다."
    "[player_name]" "(이런 모습, 꽤 보기 좋네... )"
    show chanmi at left with dissolve
    c "야, [player_name], 왜 그렇게 쳐다보고 있어? 내가 그렇게 예쁘냐? ㅋㅋ"
    c "할 일이 없으면 바비큐 준비 좀 도와줘~"

    menu:
        "예뻐 보이긴 하더라, 도와줄게!":
            "[player_name]" "예쁘긴 하더라ㅎㅎ, 도와줄게!"
            hide chanmi
            show chanmi_happy at left
            $ chanmi.increase_affection(1)
            c "뭐? 갑자기 그렇게 말하면 좀 부끄럽잖아!"
            p "(찬미는 잠시 머뭇거리며 웃음을 터트린다.)"
            c "에이, 말만 그렇게 하지 말고 손부터 움직이시죠!"
            "[player_name]" "넵 알겠습니다!! 뭘 도와주면 될까?"
            c "고기 좀 준비해줘. 양념한 거 저기 있어! 고기 구우면서 조심하고, 너무 태우지 말고~"
            "[player_name]" "내가 한때 고기 굽기 장인이었거든. 나만 믿어봐~ 특별히 보여줄게!"
            "[player_name]" "(그래도 이렇게 얘기하면서 같이 뭔가 준비하는 게 꽤 즐겁네)"
            p "[player_name](은)는 찬미와 이런저런 이야기를 나누며 고기를 굽기 시작했다."
            p "찬미의 밝은 웃음소리와 함께 바비큐 준비는 한층 더 즐거워졌다"
            

        "음 난 쉬고 싶어요~":
            "[player_name]" "(음... 솔직히 도와주는 건 좀 귀찮은데... 어떻게 말하지?)"
            "[player_name]" "에이~ 난 이런 거랑은 좀 안 맞는 스타일이라서."
            p "(장난스러운 표정을 지으며 손을 휘저어 보인다.)"
            hide chanmi
            show chanmi_sad at right
            $ chanmi.decrease_affection(1)
            c "바비큐는 다 같이 준비해야 더 맛있다고!"
            c "정말 안 도와줄 거야~? 그럼 너무 서운한데..."
            "[player_name]" "(이거... 은근히 꼽주네..)"
            "[player_name]"  "에이, 알겠어, 알겠어. 나중에 도와줄게!"
            "[player_name]"  "대신 지금은 좀 쉬는 시간이라구~"
            c "휴~ 좋아. 내가 고기 굽다가 지치면 교대 준비하고 있어!"
            "[player_name]"  "일겠어ㅋㅋ 지치면 말해!"
            "[player_name]"  "(꼭 내가 도와줘야 하는 건 아닌데... 끝까지 날 시키려는 거야? 은근히 고집 있네.)"
            p "찬미는 가볍게 한숨을 쉬며 다시 준비를 시작하고, [player_name](은)는 조용히 옆에서 지켜본다."
            

    "바비큐가 시작되고, 우리는 고기를 구우며 서로 이야기를 나누었다."
    
    s3 "[player_name]! 고기 태우지 말고 맛있게 구워봐~ (웃음)"
    menu:
        "장난으로 맞받아친다":
            "나는 학생 3에게 장난스럽게 대꾸했다."
            s3 "아하하! 역시 재밌네."
            return

        "진지하게 대꾸한다":
            "나는 진지하게 대꾸하며 고기에 더 집중했다."
            s3 "앗, 미안! 그냥 농담이었어. (웃음)"
            return

    "잠시 후, 학생 2가 내게 쌈을 싸서 내밀었다."

    menu:
        "쌈을 받아 먹는다":
            "나는 학생 2가 준 쌈을 맛있게 먹었다."
            s2 "맛있지? 더 줄까?"
            "나는 고기를 학생 2의 접시에 올려주며 고마움을 표했다."
            return

        "거절한다":
            "나는 쌈을 거절하고 고기를 굽는 데 집중했다."
            return


    scene bg_drinking_game with fade
    "바비큐가 마무리되고, 우리는 술을 마시며 게임을 시작했다."

    if affection_1 >= 10:
        "학생 1이 편의점에 가서 아이스크림과 숙취 해소제를 사왔다."
        s1 "우리 잠깐 맥주 한 잔 더 하고 들어갈까요?"
        menu:
            "같이 간다":
                "나는 학생 1과 함께 맥주를 마시며 대화를 나누었다."
                "학생 1의 다양한 이야기를 들으며 더 가까워진 느낌이었다."
                return

            "거절한다":
                "나는 잠시 쉬고 싶다며 숙소로 돌아갔다."
                return

    scene bg_beach_evening with fade
    "밤이 되자, 우리는 해변으로 산책을 나섰다."
    "술에 취한 학생 2가 걸려 넘어질 뻔했다."

    menu:
        "학생 2를 잡아준다":
            "나는 학생 2를 잡아주었다."
            s2 "고마워. 덕분에 안 넘어졌어. (미소)"
            return

        "모른 척 지나간다":
            "나는 그냥 지나쳤다. 아무 일도 없었던 것처럼 산책은 계속되었다."
            return

    "불꽃놀이를 하기로 했다."
    s3 "우리 바닷가 근처에서 더 해보는 거 어때?"

    menu:
        "좋아요":
            "나는 학생 3과 함께 바닷가 근처에서 불꽃놀이를 즐겼다."
            s3 "우와, 정말 예쁘다!"
            return

        "싫어요":
            "나는 다른 사람들과 함께 불꽃놀이를 마무리했다."
            return

    "불꽃놀이 후, 우리는 숙소로 돌아가 잠을 잤다."
    "다음 날 아침, 우리는 학교로 돌아가는 버스에 올랐다."

    return

label chapter2_end:
    $ persistent.chapter2_cleared = True  # 챕터 2 완료 상태 설정
    jump chapter3
    return
