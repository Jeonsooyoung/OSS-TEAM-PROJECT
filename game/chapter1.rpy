define p = Character(" ")
# define s1 = Character("학생 1")
# define s2 = Character("학생 2")
# define s3 = Character("학생 3")
define prof = Character("김봉재 교수님")

label chapter1:

    # 강의실에 들어서며 시나리오 시작
    scene classroom with fade
    "[player_name]" "벌써 방학이 끝났다니ㅠㅠ 2학기 시작이다"
    "[player_name]" "이번 학기에는 연애할 수 있을까?"
    p "설레는 마음으로 강의실에 들어간다"
    p "앞자리에 학생 1이 앉아 있고, 뒷자리에 학생 2가 앉아 있다"
    "[player_name]" "벌써 자리가 꽉 차 있네. 사람 없는 중간 자리에 앉아야겠다"
    
    # 학생 3과의 상호작용
    s "안녕! 여기 앉아도 돼?"
    
    menu:
        "인사를 받아준다":
            "[player_name]" "그래, 앉아."
            s "고마워! 방학 동안 잘 지냈니?" 
            $ sena.increase_affection(1) # 호감도 상승
            "[player_name]" "응, 잘 보냈어. 너는 어땠어?"
            s "나도 나름대로 재밌게 지냈어! 다음 방학에 같이 어디 놀러 가지 않을래?" 
            "[player_name]" "나야 좋지. 다음에 같이 놀러 가자!"
        "인사를 받아주지 않는다":
            "[player_name]" "여기 자리 있어서.."
            s "아, 그래... 알겠어." 
            $ sena.decrease_affection(1) # 호감도 하락
            s "뒷자리로 가야겠다." 
            
    # 교수님 등장
    p "강의실에 교수님이 들어온다"
    prof "여러분, 방학 잘 보내셨나요? 오늘은 학기의 첫날인 만큼 간단히 앞으로의 수업 계획을 설명하고, 조별 과제를 배정하도록 하겠습니다."
    "[player_name]" "아니, 첫날부터 조별 과제라니... 너무 빡센 거 아냐? 방학 끝난 지 얼마나 됐다고.ㅠㅠ"
    prof "여러분, 조별 과제는 학기 중에 진행될 주요 프로젝트입니다. 과제의 주제는 '앱 개발'이고, 조는 제가 랜덤으로 정할게요."
    prof "물론 부담스러울 수 있다는 걸 알지만, 이번 과제를 통해 여러분이 실력을 쌓고 서로 협력하는 기회를 얻길 바랍니다."
    p "제비뽑기를 통해 조가 정해졌고, 같은 조원은 [c],[a],[s]이었다"
    "[player_name]" "(어떤 사람들과 한 조가 될지 걱정했는데, 조원들이 나쁘지 않아서 다행이다.)"
    c "안녕! 같은 조가 됐네. 난 [c]이야. 앞으로 잘 부탁해!"  
    "[player_name]" "응, 잘 부탁해. 난 [player_name]이야."  
    a "난 [a]라고 해. 조별 과제는 솔직히 부담스럽지만... 다들 화이팅 해보자.ㅎㅎ" 
    s "와, 팀 분위기 좋은데? 난 [s]! 힘든 과제라도 다 같이 하면 재밌을 거야!"  
    # 조 주제 결정
    c "우리 어떤 앱을 만들지 주제를 정해야 하는데, 다들 좋은 아이디어 있어?"
    c "나는 게임 앱을 개발하는 게 좋을 것 같아. 그렇게 복잡하지도 않고, 잘할 수 있을 것 같거든."
    a "나는 파트 타임 스터디 같은 공부 시간 기록 앱을 생각해 봤어."
    s "이 주제는 어때? 언제 몇 번 빠졌는지 체크해주는 출석부 앱이야."
    
menu:
    "여학생들의 의견을 따른다":
        "[player_name] 우와! 다들 아이디어가 넘치네. 나는 이중에서.."
        
        # 여학생들의 의견에 따른 세부 주제 선택
        menu:
            "게임 앱":
                $ final_topic = "게임 앱"
                "[player_name] 나는 게임 앱이 제일 좋아 보여."
                jump continue_story
            "공부 시간 기록 앱":
                $ final_topic = "공부 시간 기록 앱"
                "[player_name] 나는 공부 시간 기록 앱이 가장 실용적일 것 같아."
                jump continue_story
            "출석부 앱":
                $ final_topic = "출석부 앱"
                "[player_name] 나는 출석부 앱이 제일 유용할 것 같아."
                jump continue_story
    "다른 의견을 낸다":
        "[player_name] 다들 좋은 아이디어지만 나는 사실 요리 앱도 좋을 것 같아. 사용자에게 레시피를 알려주고, 필요한 재료를 쉽게 찾을 수 있게 도와주는 앱이라면 흥미롭지 않을까?"
        $ final_topic = "요리 앱"
        c "오, 요리 앱이라니 너무 흥미로운데? 이걸로 가는거 어때?"
        a "좋아! 앞으로의 프로젝트가 너무 기대되는걸?"
        s "우리 조 정말 대단한데! 교수님도 감탄하며 박수를 보내실 것 같아.~"
        jump continue_story

label continue_story:
    c "좋아. 이제 우리가 선택한 주제로 앱을 만들어 보자!"
    prof "자, 다들 주제는 정했나요? 오늘 수업은 여기까지 할게요. 여러분이라면 멋진 발표를 준비해 올 거라 믿어요. 다음 수업에서 기대할게요~!"
    p "수업이 끝나고 집으로 돌아온다."
    return


    # 팀 해산 후, 채팅
    p "그날 밤, 단체 채팅방에서 조별 과제와 관련된 이야기를 나누기로 했다."
    c "조별 과제는 어떻게 나눠서 할지 이야기해 볼까? 각자 맡고 싶은 부분이 있으면 말해줘!"
    c "나는 발표 쪽이 좋아! 말하는 건 자신 있으니까 그 부분은 내가 맡을게."
    a "나는 자료 조사랑 PPT 제작을 맡을게. 꼼꼼하게 만드는 거 자신 있어!"

    menu:
        "좋다":
            p "알겠어. 내가 도와줄게."
            c "정말 고마워요!" 
            $ chanmi.increase_affection(1) # 호감도 상승
        "싫다":
            p "미안, 지금은 바빠."
            c "아, 알겠어요..." 
            $ chanmi.decrease_affection(1) # 호감도 하락

    # 발표 연습
    p "발표자는 제비뽑기로 정하기로 했고, 나와 학생 2가 발표자로 뽑혔다."
    p "발표 연습 중, 학생 2가 제안했다."
    a "여기 부분은 이렇게 하는 게 어때요?"
    
    menu:
        "제안을 받아들인다":
            p "좋은 생각이야."
            a "고마워! 같이 더 완벽히 만들자." 
            $ ari.increase_affection(1) # 호감도 상승
        "제안을 거절한다":
            p "내 생각엔 그냥 이렇게 하는 게 나아."
            a "아, 알겠어..." 
            $ ari.decrease_affection(1) # 호감도 하락

    # 발표 성공
    p "발표는 성공적으로 마무리되었고, 교수님께 좋은 평가를 받았다."
    prof "잘했어요! 여러분 팀워크가 돋보이는 좋은 발표였어요."

    p "이렇게 Chapter 1이 끝났다."
    
    return
