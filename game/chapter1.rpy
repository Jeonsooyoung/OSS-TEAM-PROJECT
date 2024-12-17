define p = Character(" ")
# define s1 = Character("학생 1")
# define s2 = Character("학생 2")
# define s3 = Character("학생 3")
define prof = Character("김봉재 교수님")
image man = "character/man_extra.png"
image classroom = "background/classroom.png"
image home = "background/home.jpg"
image campus = "background/campus.jpg"
image story_end = "background/background.png"

label chapter1:
    $ load_game_state()
    $ sync_player_name()

    # 나머지 코드...
    # 충북대에 들어서며 시나리오 시작

    scene campus with fade
    p "여름이 끝나고 선선한 가을바람이 부는 캠퍼스. 나무는 초록에서 서서히 단풍으로 물들고 있다."
    p "충북대 정문에서 잠시 걸음을 멈춘다"
    "[player_name]" "익숙한 길, 익숙한 풍경이지만 뭔가 다르게 느껴지네."
    "[player_name]" "주변에 활기찬 학생들을 보니 2학기가 기대되는걸?"
    "[player_name]" "그나저나 2학기가 되니까 1학기 보다 연애하는 학생들의 수가 엄청 늘어난 것 같아... 나도 이번 학기에는 연애할 수 있을까?"
    "걱정을 하다 시계를 보니 어느세 지각하기 직전이다"
    "[player_name]" "으악! 지각이다!"
    p "2학기, [player_name](이)의 새로운 이야기 막이 오른다."

    play music "audio/normal.ogg" fadein 5.0
    # 강의실에 들어서며 시나리오 시작
    scene classroom with fade
    p "허겁지겁 강의실에 들어간다"
    "[player_name]" "벌써 자리가 꽉 차 있네. 사람 없는 중간 자리에 앉아야겠다"
    
    # 학생 3과의 상호작용
    show chanmi at left with dissolve
    c "안녕! 여기 앉아도 돼?"
    
    menu:
        c "안녕! 여기 앉아도 돼?{fast}" # 선택지가 나와도 대화창이 남아있음
        "인사를 받아준다":
            "[player_name]" "그래, 앉아."
            "[player_name]" "응, 잘 보냈어. 너는 어땠어?"
            hide chanmi
            show chanmi_happy at left
            c "고마워! 방학 동안 잘 지냈니?" 
            $ chanmi.increase_affection(15) # 호감도 상승
            c "나도 나름대로 재밌게 지냈어! 다음 방학에 같이 어디 놀러 가지 않을래?" 
            "[player_name]" "나야 좋지. 다음에 같이 놀러 가자!"
            hide chanmi_happy
        "인사를 받아주지 않는다":
            "[player_name]" "여기 자리 있어서.."
            $ chanmi.decrease_affection(10) # 호감도 하락
            hide chanmi
            show chanmi_sad at left
            c "아, 그래... 알겠어." 
            c "뒷자리로 가야겠다." 
            hide chanmi_sad

    # 교수님 등장
    p "강의실에 교수님이 들어온다"
    show man at center, small_size
    prof "여러분, 방학 잘 보내셨나요? 오늘은 학기의 첫날인 만큼 간단히 앞으로의 수업 계획을 설명하고, 조별 과제를 배정하도록 하겠습니다."
    "[player_name]" "아니, 첫날부터 조별 과제라니... 너무 빡센 거 아냐? 방학 끝난 지 얼마나 됐다고ㅠㅠ"
    prof "여러분, 조별 과제는 학기 중에 진행될 주요 프로젝트입니다. 과제의 주제는 '앱 개발'이고, 조는 제가 랜덤으로 정할게요."
    prof "물론 부담스러울 수 있다는 걸 알지만, 이번 과제를 통해 여러분이 실력을 쌓고 서로 협력하는 기회를 얻길 바랍니다."
    hide man
    p "제비뽑기를 통해 조가 정해졌고, 같은 조원은 [c],[a],[s]였다"
    "[player_name]" "(어떤 사람들과 한 조가 될지 걱정했는데, 조원들이 나쁘지 않아서 다행이다.)"
    show chanmi at left 
    c "안녕! 같은 조가 됐네. 난 [c]야. 앞으로 잘 부탁해!"  
    "[player_name]" "응, 잘 부탁해. 난 [player_name]이야."  
    show ari at center 
    a "난 [a]라고 해. 조별 과제는 솔직히 부담스럽지만... 다들 화이팅 해보자.ㅎㅎ" 
    show sena at right
    s "와, 팀 분위기 좋은데? 난 [s]! 힘든 과제라도 다 같이 하면 재밌을 거야!"  
    # 조 주제 결정
    c "우리 어떤 앱을 만들지 주제를 정해야 하는데, 다들 좋은 아이디어 있어?"
    c "나는 게임 앱을 개발하는 게 좋을 것 같아. 그렇게 복잡하지도 않고, 잘할 수 있을 것 같거든."
    a "나는 파트 타임 스터디 같은 공부 시간 기록 앱을 생각해 봤어."
    s "이 주제는 어때? 언제 몇 번 빠졌는지 체크해주는 출석부 앱이야."
    
menu:
    s "이 주제는 어때? 언제 몇 번 빠졌는지 체크해주는 출석부 앱이야.{fast}"
    "여학생들의 의견을 따른다":
        "[player_name]" "우와! 다들 아이디어가 넘치네. 나는 이중에서.."
        
        # 여학생들의 의견에 따른 세부 주제 선택
        menu:
            "게임 앱":
                $ final_topic = "게임 앱"
                "[player_name]" "나는 게임 앱이 제일 좋아 보여."
                jump continue_story
            "공부 시간 기록 앱":
                $ final_topic = "공부 시간 기록 앱"
                "[player_name]" "나는 공부 시간 기록 앱이 가장 실용적일 것 같아."
                jump continue_story
            "출석부 앱":
                $ final_topic = "출석부 앱"
                "[player_name]" "나는 출석부 앱이 제일 유용할 것 같아."
                jump continue_story
    "다른 의견을 낸다":
        "[player_name]" "다들 좋은 아이디어지만 나는 사실 요리 앱도 좋을 것 같아. 사용자에게 레시피를 알려주고, 필요한 재료를 쉽게 찾을 수 있게 도와주는 앱이라면 흥미롭지 않을까?"
        $ final_topic = "요리 앱"
        c "오, 요리 앱이라니 너무 흥미로운데? 이걸로 가는거 어때?"
        a "좋아! 앞으로의 프로젝트가 너무 기대되는걸?"
        s "우리 조 정말 대단한데! 이 정도면 교수님도 감탄하실 것 같아~."
        jump continue_story

label continue_story:
    c "좋아. 이제 우리가 선택한 주제로 앱을 만들어 보자!"
    hide chanmi
    hide ari
    hide sena with dissolve
    show man at center, small_size
    prof "자, 다들 주제는 정했나요? 오늘 수업은 여기까지 할게요. 여러분이라면 멋진 발표를 준비해 올 거라 믿어요. 다음 수업에서 기대할게요~!"
    hide man
    p "수업이 끝나고 집으로 돌아온다."

    scene home with fade

    # 팀 해산 후, 채팅
    p "그날 밤, 단체 채팅방에서 PPT와 관련된 이야기를 나누기로 했다."
    window hide
    label phone_example:
    # 대화 데이터를 정의
    $ phone_dialogue = [
        Dialogue("세나", "안녕?", current=True),
        Dialogue("[player_name]", "안녕!", current=False),
        Dialogue("찬미", "조별 과제는 어떻게 나눠서 할지 이야기해볼까? 각자 맡고 싶은 부분이 있으면 말해줘!", current=False),
        Dialogue("찬미", "나는 발표 쪽이 좋아! 말하는 건 자신 있으니까 그 부분은 내가 맡을게.", current=False),
        Dialogue("세나", "나는 PPT 제작 맡을게. 꼼꼼하게 만드는 거 자신 있어!", current=False),
        Dialogue("아리", "음... 그럼 나는 자료 조사를 하면 될까? 열심히 찾아볼게", current=False),
        Dialogue("[player_name]", "좋아! 그럼 발표는 내가 찬미누나랑 함께 맡을게. 그리고 자료 정리 마감일은 내일까지로 하자. 모두 힘내서 멋지게 해보자!", current=False)
    ]

    # PhoneDialogue 화면을 호출
    show screen phone_dialogue(dialogue=phone_dialogue)

    # 대사가 하나씩 출력되도록
    $ next_message(phone_dialogue)  # 첫 번째 대사 출력

    # 대사 진행을 위해 클릭 대기
    label wait_for_click:
        # 대사 진행 상태를 확인
        $ current_dialogue = [d for d in phone_dialogue if d.current]
        
        # 만약 대사가 끝났으면 다음 대사를 출력
        if current_dialogue:
            $ next_message(phone_dialogue)
            pause  # 플레이어의 클릭을 기다리기 위해 잠시 대기
            jump wait_for_click  # 클릭 후 계속 진행

    # 대사가 모두 끝나면 화면을 숨김
    hide screen phone_dialogue


    p "조별 과제 분담 이야기가 끝난 뒤, 아리가 따로 자료조사를 도와달라는 메시지를 보내왔다."

    label phone_example2:
        # 대화 데이터를 정의
        $ phone_dialogue = [
        Dialogue("아리", "저기, 잠깐 시간 괜찮아? 사실 자료 조사하다가 조금 막히는 부분이 있어가지고...", current=True),
        Dialogue("아리", "괜찮다면 자료 찾는 거 도와줄 수 있을까?", current=True),
        ]
        # PhoneDialogue 화면을 호출
        show screen phone_dialogue(dialogue=phone_dialogue)

        # 플레이어가 상호작용할 시간을 줌
        pause
        window show
        menu:
            a "괜찮다면 자료 찾는 거 도와줄 수 있을까?{fast}"

            "도와준다":
                window hide
                $ phone_dialogue.append(Dialogue("[player_name]", "알겠어. 내가 도와줄게. 어떤 자료 찾으면 될까?",current=True))
                $ phone_dialogue.append(Dialogue("아리","우와 정말 고마워!",current=True))
                $ ari.increase_affection(15) # 호감도 상승
                $ phone_dialogue.append(Dialogue ("아리","우리 팀 주제가 [final_topic]이니까 개발 동기, 과제 수행 방법, 예측되는 문제점을 찾아줄 수 있을까?",current=True))
                $ phone_dialogue.append(Dialogue ("[player_name]", "혼자 자료조사 하기 힘들었겠다ㅠㅠ 최대한 빨리 찾아서 너한테 보내줄게",current=True))
                $ phone_dialogue.append(Dialogue ("아리","응! 덕분에 한결 마음이 편해진다 도와줘서 고마워!",current=True))

                p "보내준 자료 덕분에 아리는 자료 조사를 훨씬 수월하게 진행할 수 있었다. 그녀가 만족스러워하는 모습이 머릿속에 그려지는 듯했다."
        
            "도와주지 않는다":
                window hide
                $ phone_dialogue.append(Dialogue ("[player_name]", "미안해... 지금은 좀 바빠서 도와주기 어려울 것 같아. 다음엔 꼭 도와줄게!",current=True))
                $ ari.decrease_affection(10) # 호감도 하락
                $ phone_dialogue.append(Dialogue ("아리","아, 알겠어...어쩔 수 없지, 그래도 답장해줘서 고마워",current=True))
                
        # PhoneDialogue 화면을 호출
        # show screen phone_dialogue(dialogue=phone_dialogue)

        # 플레이어가 상호작용할 시간을 줌
        # pause

        # 화면 닫기
        hide screen phone_dialogue

    
    # 세나와 주인공의 대화(ppt)
    p "휴대폰이 진동하며 화면에 알림이 떴다. 세나가 보낸 메시지였다."
    window hide
    label phone_example3:
        # 대화 데이터를 정의
        $ phone_dialogue = [
        Dialogue("세나", "지금 PPT 디자인을 손보고 있는데, 네 의견이 듣고 싶어서 연락했어.", current=True),
        Dialogue("세나", "내가 골라본 색 조합이 괜찮은지 모르겠어. 혹시 한 번 봐줄 수 있을까?", current=True),
        ]
        # PhoneDialogue 화면을 호출
        show screen phone_dialogue(dialogue=phone_dialogue)

        # 플레이어가 상호작용할 시간을 줌
        pause

        window show
        menu:
            s "내가 골라본 색 조합이 괜찮은지 모르겠어. 혹시 한 번 봐줄 수 있을까?{fast}"

            "적극적으로 반응한다":
                window hide
                $ phone_dialogue.append(Dialogue ("[player_name]", "물론이지! 내가 한번 볼게. 세나라면 분명 잘 만들었을 것 같은데?",current=True))
                $ sena.increase_affection(15) # 호감도 상승
                $ phone_dialogue.append(Dialogue ("세나","고마워! 사실 표지에 이 색 조합 쓰는 게 어떨까 싶었어. 좀 단순한 느낌일까?",current=True))
                $ phone_dialogue.append(Dialogue ("[player_name]", "아니야, 색 조합 괜찮아! 근데 조금 더 강조하고 싶으면 글자 테두리를 추가해보는 것도 좋을 것 같아.",current=True))
                $ phone_dialogue.append(Dialogue ("세나","오! 좋은 생각이야. 바로 적용해볼게!",current=True))
                $ phone_dialogue.append(Dialogue ("세나","덕분에 내가 원하던 느낌 그대로 PPT를 완성할 수 있을 것 같아! 고마워.",current=True))
                $ phone_dialogue.append(Dialogue ("[player_name]", "그래! 의견 묻고 싶은 거 있으면 언제든 말해.",current=True))
                p "[player_name]의 조언 덕분에 세나는 PPT 디자인에 더욱 의욕적으로 임했다."

                
            "무시한다":
                window hide
                "[player_name]" "읽기 귀찮은데.."
                "[player_name]""(세나가 보낸 메시지를 읽어보지만, 답장은 하지 않기로 한다.)"
                $ sena.decrease_affection(10) # 호감도 하락
                p "세나가 보낸 메시지는 그대로 방치되었고, [player_name]는(은) 신경을 쓰지 않았다."
                s "(음... 아무래도 답장이 없네. 괜히 물어본 걸까?)"
                p "세나는 살짝 실망한 듯 보였다."
                
        
        # PhoneDialogue 화면을 호출
        show screen phone_dialogue(dialogue=phone_dialogue)

        # 플레이어가 상호작용할 시간을 줌
        pause

        # 화면 닫기
        hide screen phone_dialogue

    label phone_example4:
        # 대화 데이터를 정의
        $ phone_dialogue = [
        Dialogue("찬미", "발표 준비 같이 하게 돼서 좋다! 발표 내용은 어떻게 나눠서 할지 이야기해보자.", current=True),
        Dialogue("[player_name]", "좋아요. 누나 맡고 싶은 부분 있어요?", current=True),
        Dialogue("찬미","음... 나는 PPT 내용 중에서 주제에 대한 설명 부분이 좋을 것 같아. 내가 개발 동기, 앱 설명 부분을 맡을게.",current=True),
        Dialogue("찬미","그럼 [player_name]은(는) 나머지 부분을 맡을래?",current=True),
        ]
        # PhoneDialogue 화면을 호출
        show screen phone_dialogue(dialogue=phone_dialogue)

        # 플레이어가 상호작용할 시간을 줌
        pause
        window show
        menu:
            c "그럼 [player_name]은(는) 나머지 부분을 맡을래?{fast}"

            "좋아요! 제가 나머지 부분 맡을게요!":
                window hide
                $ phone_dialogue.append(Dialogue ("[player_name]", "좋아요! 나머지 부분은 제가 맡을게요.",current=True))
                $ chanmi.increase_affection(15) # 호감도 상승
                $ phone_dialogue.append(Dialogue ("찬미","고마워! 함께 잘 준비하자!",current=True))
                "[player_name]" "누나는 내가 맡은 부분을 맡아줘서 고마운 듯 보였다."
                p "발표 준비는 놀라울 정도로 수월했고, 우리는 점점 더 서로에게 의지하게 되는 것 같았다."
                
            "이 부분하기 싫은데...":
                window hide
                "[player_name]" "음... 저도 사실 누나랑 같은 부분 하고 싶어요."
                $ chanmi.decrease_affection(10)  # 호감도 하락
                $ phone_dialogue.append(Dialogue ("찬미", "아, 그래? 그럼 다른 방식으로 나누자. 괜찮아.",current=True))
                p "찬미는 살짝 아쉬워하는 듯했지만, 그래도 다른 방법을 찾기로 했다."
                $ phone_dialogue.append(Dialogue ("찬미", "어느 부분 맡고 싶은데?",current=True))
                $ phone_dialogue.append(Dialogue ("[player_name]", "앱 설명 부분을 맡고 싶어요..!",current=True))
                $ phone_dialogue.append(Dialogue ("찬미", "알겠어! 내가 소개와 결론을 맡고, 네가 앱을 소개하는 부분을 맡자.",current=True))
                $ phone_dialogue.append(Dialogue ("찬미", "네가 맡게 될 부분은 정말 중요하니까 열심히 준비해줘!",current=True))
                $ phone_dialogue.append(Dialogue ("[player_name]", "넵. 열심히 준비할게요. 양보해 줘서 고마워요!",current=True))
                $ phone_dialogue.append(Dialogue ("찬미", "그래, 우리 잘 해보자!",current=True))
                p "찬미의 아쉬움은 잠시였지만 그래도 서로의 역할을 나누고 함께하는 모습에, 조금은 더 가까워졌다."
                
        
        # PhoneDialogue 화면을 호출
        show screen phone_dialogue(dialogue=phone_dialogue)

        # 플레이어가 상호작용할 시간을 줌
        pause

        # 화면 닫기
        hide screen phone_dialogue

    window show

    # 발표 성공
    scene classroom
    prof "여러분, 프로젝트 준비 잘 하셨나요? 저는 여러분이 잘 준비했을 거라고 믿어요. 그럼, 1조부터 발표를 시작하겠습니다."
    p "발표는 성공적으로 마무리되었고, 교수님께 좋은 평가를 받았다."
    prof "정말 잘했어요! 여러분의 팀워크가 빛나는 발표였습니다."
    p "[player_name]의 팀은 좋은 점수를 받았다. 모두 환하게 웃으며 서로를 축하했다"
    p "그 미소 속에는 기쁨과 함께 조금은 떨리는 마음이 섞여 있었다."
    hide classroom # 모든 캐릭터 숨기기
    show story_end
    p "Chapter 1 종료"

    jump chapter1_end 
    stop music fadeout 5.0

    return

label chapter1_end:
    $ persistent.chapter1_cleared = True  # 챕터 1 완료 상태 설정
    $ save_game_state()
    # call screen chapter_select
    jump chapter2

    return