#나레이션
define p = Character(" ")

image library = "background/library.jpg"
image library2 = "background/library2.jpg"
image cafe = "background/cafe.jpg"
image coffee_machine = "background/coffee_machine.jpg"

label chapter3:

    $ load_game_state()
    $ sync_player_name()

    "[player_name]" "하.. x발 벌써 중간고사네..."
    "[player_name]" "도서관가서 공부나 해야겠다."

    narrator "{fast}도서관으로 이동 중...{slow=0.05}"

    show library with fade
    "[player_name]" "사람들 공부 열심히들 하시네.. 근데 어디에 앉지.."
    "[player_name]" "역시 나는 구석으로 가야겠다."
    show library2 with fade
    show chanmi at left
    show ari at right
    #자리에 앉은 장면
    "[player_name]""어 뭐야 찬미누나도 공부하려고 도서관에 왔네"
    p"[player_name]은(는) 찬미에게 손인사를 한다. 아리도 인사를 받아준다"
    hide ari
    show chanmi at right with move
    p"[player_name]이(가) 공부를 하던중, 찬미가 노트를 들고 다가온다"
    c "[player_name]!! 혹시 이거 좀 봐줄래..? 내가 제대로 정리한 건지 모르겠어."
    
    menu:
        c "[player_name]!! 혹시 이거 좀 봐줄래..? 내가 제대로 정리한 건지 모르겠어.{fast}"
        "확인하고 칭찬한다":
            "[player_name]""와.. 누나 완전 대단하다. 이 정도면 완벽한거 같은데?"
            hide chanmi
            show chanmi_happy at right with dissolve
            $ chanmi.increase_affection(1)
            c "아 ㅎㅎ!! 진짜 고마워!!"
            c "너랑 얘기하니까 마음이 좀 놓인다..."
            hide chanmi_happy
            show chanmi at right with dissolve
            c "우리 공부 다 끝내고 같이 밥먹을래??."
            
            menu:
                "좋아":
                    "[player_name]""좋아. 같이 먹을 사람 없었는데 다행이다."
                    hide chanmi
                    show chanmi_happy at right with dissolve
                    c "오~~ [player_name]!! 이따 공부 끝나면 연락해!!"
                    "[player_name]""그래 이따 연락할게!"
                    $ chanmi.increase_affection(1)
                    hide chanmi_happy
                "혼밥해":
                    "[player_name]""누나랑 밥먹어줄 사람 없어용~~"
                    hide chanmi
                    show chanmi_sad at left with dissolve
                    c "아.. 알겠어.."
                    $ chanmi.decrease_affection(2)
                    p "찬미는 짜증내며 자리로 돌아간다."
                    hide chanmi_sad
                "미안해":
                    "[player_name]""미안.. 나 선약이 있어"
                    c"그래? 아쉽지만 어쩔 수 없네"
                    p "찬미는 아쉬워하며 자리로 돌아간다."
                    hide chanmi

        "찬미교수..":
            "[player_name]""이 노트로 교수님이 배워야 하는거 아니야...? 찬미교수님?"
            hide chanmi
            show chanmi_happy at right with dissolve
            $ chanmi.increase_affection(1)
            c "아 ㅋㅋㅋㅋㅋ 어이없다. 너 진짜 못말려~~ 아잉~~"
            p "찬미는 한층 밝아진 표정으로 자리로 돌아간다."
            hide chanmi_happy

        "별로야":
            "[player_name]""정리가 많이 아쉽네. 다시 해보길 바래"
            hide chanmi
            show chanmi_sad at left with dissolve
            $ chanmi.decrease_affection(1)
            c"너 너무한거 아니니!!"
            p "찬미는 화난 표정으로 자리로 돌아간다."
            hide chanmi_sad
    
    show ari at left with move
    p"[player_name]이(가) 조용히 공부하던 중 아리가 갑자기 어깨를 툭툭 친다"

    a"이 문제 좀 봐줄래..? 나 머리가 잘 안돌아가.."

    menu:
        a"이 문제 좀 봐줄래..? 나 머리가 잘 안돌아가..{fast}"
        "문제를 봐준다":
            p "아리 옆으로 다가가 문제를 도와준다"
            hide ari
            show ari_happy at right with dissolve
            a"와 너 덕분에 진짜 살았다.. 진짜 고마워!"
            $ ari.increase_affection(1)
            "[player_name]""별거 아니라구 ㅋ"
            hide ari_happy

        "멍청아":
            "[player_name]""넌 머리가 안돌아가는게 아니라. 멍청한거야"
            a"머..뭐라고..?"
            "[player_name]""장난이고 이미 과부화 걸린거야. 좀 쉬면서해"
            a"그래 너 정말 태평하다! ㅋㅋㅋㅋ"
            p "아리가 다시 자리로 돌아가 다시 문제를 고민한다"
            hide ari with dissolve

        "다음에 알려줄게":
            "[player_name]""내 문제도 많이 밀려 있어서.. 나중에 알려줄게!"
            a"내일 모레 시험인데.. 알았어!!"
            hide ari
            show ari_sad at right with dissolve
            $ ari.decrease_affection(1)
            "아리는 다른 사람을 찾아 떠난다."
            hide ari_sad

    "[player_name]""다시 열심히 공부해볼까?"
    #3hours later
    "[player_name]은(는) 공부를 열심히 하다 잠깐 쉬러 나왔다."
    show sena at right
    "[player_name]""어, 세나야 안녕!!"
    p "세나가 인사를 하며 다가왔다."
    s"공부 많이했어?"
    "[player_name]""어.. 나 오늘 하루종일 도서관에 있었다.."
    "[player_name]""지금 잠깐 쉬러 나왔어"
    s "너무 열심히 하는 거 아니야? 좀 쉬면서해~~ 커피 한 잔 사줄게."
    
    menu:
        s "너무 열심히 하는 거 아니야? 좀 쉬면서해~~ 커피 한 잔 사줄게.{fast}"
        "좋은데?":
            "[player_name]""어어 너무 좋다. 가자가자"
            s "좋아, 잠깐 머리 식히는 것도 필요하잖아."
            show coffee_machine with fade
            show sena at right
            p "둘은 커피 자판기로 이동하며 대화를 나눈다."
            menu:
                p "둘은 커피 자판기로 이동하며 대화를 나눈다.{fast}"
                "시험 이후 계획에 대해 묻는다":
                    "[player_name]" "시험 끝나면 뭐 할 계획이야?"
                    s "나는 무조건 여행 갈 거야. 너도 같이 갈래?"
                    
                    menu:
                        s "나는 무조건 여행 갈 거야. 너도 같이 갈래?{fast}"
                        "농담으로 응답한다":
                            "[player_name]" "네가 다 계획했구나. 난 네가 운전만 해주면 따라갈게."
                            hide sena
                            show sena_happy at right with dissolve
                            s "좋아, 넌 그냥 옆에서 초콜릿만 먹고 있어."
                            $ sena.increase_affection(1)
                            hide sena_happy with dissolve
                        "진지하게 관심을 보인다":
                            "[player_name]" "생각해볼게. 근데 어디로 가려고?"
                            hide sena
                            show sena_happy at right with dissolve
                            $ sena.increase_affection(2)
                            s "제주도로 갈 생각이었어."
                            "[player_name]""와 나도 제주도 가고싶었는데!! 내가 한번 계획짜볼게!"  
                            "[player_name]" "세나의 열정을 보며 나도 설렜다."
                            hide sena_happy with dissolve

                "최근 스트레스에 대해 이야기한다":
                    "[player_name]" "하.. 요즘 스트레스 너무 많다."
                    s "나도 그래. 이번 시험이 끝나면 진짜 쉬고 싶어.."
                    
                    menu:
                        s "나도 그래. 이번 시험이 끝나면 진짜 쉬고 싶어..{fast}"
                        "고마워하며 말을 꺼낸다":
                            "[player_name]""너도 힘든데 이렇게 챙겨줘서 고마워."
                            hide sena
                            show sena_happy at right with dissolve
                            $ sena.increase_affection(2)
                            s "네가 이렇게 말해주니까 더 힘내야겠다는 생각이 든다.. ㅎㅎ"
                            hide sena_happy with dissolve
                        "농담으로 분위기를 바꾼다":
                            "[player_name]" "시험 끝나면 우리 둘 다 바로 지쳐 쓰러지겠지?"
                            hide sena
                            show sena_happy at right with dissolve
                            $ sena.increase_affection(1)
                            s "우린 멋지게 쓰러질 것 같아 하하하하하~"
                            hide sena_happy with dissolve
                        "아닌데? ㅋ" :
                            "[player_name]""난 시험 끝나고도 계속 공부 할건데?"
                            hide sena
                            show sena_sad at left with dissolve
                            $ sena.decrease_affection(1)
                            s"아.. 그래 그러던가;;"
                            hide sena_sad with dissolve 
        
        "괜찮아 ㅎㅎ":
            p "지금은 좀 힘들어. 나 다시 바로 공부하러 가야하거든..."
            hide sena
            show sena_sad at right with dissolve
            $ sena.decrease_affection(1)
            s "그래..? 다른 사람이랑 가야겠네.."
            hide sena_sad

        "커피를 사 주겠다고 한다":
            "[player_name]" "내가 살게! 나도 커피가 땡기던 참이었어."
            hide sena
            show sena_happy at right with dissolve
            $ sena.increase_affection(3)
            "[player_name]""쿠비앤용으로 가자!"
            s "역시 넌 너무 착해. 넌 너무 빛이나.."
            hide sena_happy
            show cafe with fade
            show sena at right with dissolve
            p "둘은 커피를 마시며 가볍게 이야기를 나눴다."
            s "근데 너 우리과 중에서 제일 친하다고 생각하는 사람 있어?"
            
            menu:
                s "근데 너 우리과 중에서 제일 친하다고 생각하는 사람 있어?{fast}"
                "너라고 답한다":
                    "[player_name]""나는 너랑 제일 친하다고 생각해. 너가 제일 편하기도 하고"
                    $ sena.increase_affection(1)
                    s "진짜? 그런 줄 몰랐네. 고맙다. 네가 이렇게 말해주니 좀 설레네..."
                "나 찐따야..":
                    "[player_name]""나... 아무랑도 친하다고 생각한적이 없어.."
                    "[player_name]""나는 찐.따.거든.."
                    s "아 그래..? 난 너랑 친하다고 생각했는데.."
                    $ sena.decrease_affection(1)
                "잘 모르겠어":
                    "[player_name]" "좀 고르기 어려운데..."
                    s "알겠어 ㅋㅋㅋㅋㅋ 내가 첫 번째 후보라고 생각할게!"

    "이렇게 [player_name]은(는) 잠시 휴식을 취하며 다시 공부에 집중할 수 있었다."
    # 늦은 밤 도서관
    "[player_name]" "늦은 밤이 되어 도서관을 나서려던 순간 찬미와 아리를 발견했다."
    
    menu:
        "찬미에게 말을 건다":
            "[player_name]""어! 이제 집가는 거야?"
            c "그럴려고, 근데 아직 안 갔네? 오늘 공부 많이 했어?"
            menu:
                "많이 했어":
                    "[player_name]""오늘 좀 많이 한거 같아 좀 피곤하네 ㅎㅎ"
                    c"고생했아 [player_name]! 과탑하는거 아니야??"
                    "[player_name]""ㅋㅋㅋㅋ 되려나.."
                    c"나 이제 집가볼게 안녕~"
                    menu:
                        "같이 가자고 한다":
                            "[player_name]""누나! 우리 같이가자! 집방향이 같으니까.."
                            c"어? 그래그래 좋아 같이가자"
                            $ chanmi.increase_affection(1)
                            "둘은 헤어지고 [player_name]은(는) 집에 도착했다"
                        "인사한다":
                            "[player_name]""응 잘가! 수업때 보자"
                            c"그래 빠이빠이~"
                            "[player_name]은(는) 쓸쓸하게 집에 도착했다"
                "아니 딴짓했어":
                    "[player_name]""아니 나 딴짓밖에 안했다.."
                    "[player_name]""(사실 공부 미친듯이 했지롱 ㅋㅋ)"
                    $ chanmi.decrease_affection(1)
                    c"아 그래?? (뭐야 열심히 하는줄 알았더니..)"
                    c"그럼 집 잘가~!"
        
        "아리에게 말을 건다":
            a "너도 이제 집 가나? 근처 편의점 들러서 뭐 좀 먹을래?"
            
            menu:
                a "너도 이제 집 가나? 근처 편의점 들러서 뭐 좀 먹을래?{fast}"
                "편의점에 간다":
                    "[player_name]""좋아 좋아 마침 출출했는데"
                    $ sena.increase_affection(1)
                    p"둘은 편의점에서 먹을 것들을 사고 테이블에 앉았다"
                    a "이 초콜릿 내가 재알 좋아하는건데 너도 먹어볼래?"
                    "[player_name]""어 먹어볼래"
                    "[player_name]와(과) 아리는 다 먹은후 편의점에서 나왔다."
                    a"잘가! 수업때 보자"
                    "[player_name]은(는) 배부른 상태로 집에 도착했다"
                "거절한다":
                    "[player_name]""미안 집에 빨리 가야해서.. 미안해!"
                    a "그래, 알았어. 그럼 내일 보자!"
                    p "아리는 아쉬운 듯 혼자 편의점으로 향했다."
                    "[player_name]은(는) 집에 도착했다"
    
    # 엔딩 분기 준비
    p "이렇게 하루가 지나갔다. 앞으로 무슨일이 생길까..?"
    
    jump chapter3_end

    return

label chapter3_end:
    $ persistent.chapter3_cleared = True  # 챕터 3 완료 상태 설정
    jump chapter4
    return