#나레이션
define p = Character(" ")

label chapter3:

    $ load_game_state()
    $ sync_player_name()

    "[player_name]" "하.. x발 벌써 중간고사네..."
    "[player_name]" "도서관가서 공부나 해야겠다."

    narrator "{fast}도서관으로 이동 중...{slow=0.05}"

    "[player_name]" "사람들 공부 열심히들 하시네.. 근데 어디에 앉지.."
    "[player_name]" "역시 나는 구석으로 가야겠다."

    #자리에 앉은 장면
    "[player_name]""어 뭐야 찬미도 공부하려고 도서관에 왔네"
    p"[player_name]은(는) 찬미에게 손인사를 한다. 아리도 인사를 받아준다"

    "[player_name]이(가) 공부를 하던중, 찬미가 노트를 들고 다가온다"
    c "[player_name]!! 혹시 이거 좀 봐줄래..? 내가 제대로 정리한 건지 모르겠어."
    
    menu:
        "확인하고 칭찬한다":
            "[player_name]""와.. 너 완전 대단하다. 이 정도면 완벽한거 같은데?"
            $ chanmi.increase_affection(1)
            c "아 ㅎㅎ!! 진짜 고마워!!"
            c "너랑 얘기하니까 마음이 좀 놓인다..."
            c "우리 공부 다 끝내고 같이 밥먹을래??."
            
            menu:
                "좋아":
                    "[player_name]""좋아. 같이 먹을 사람 없었는데 다행이다."
                    c "오~~ [player_name]!! 이따 공부 끝나면 연락해!!"
                    "[player_name]""그래 이따 연락할게!"
                    $ chanmi.increase_affection(1)
                "혼밥해":
                    "[player_name]""너랑 밥먹어줄 사람 없다~~"
                    c "아.. 알겠어.."
                    $ chanmi.decrease_affection(2)
                    p "찬미는 짜증내며 자리로 돌아간다."
                "미안해":
                    "[player_name]""미안.. 나 선약이 있어"
                    c"그래? 아쉽지만 어쩔 수 없네"
                    "찬미는 아쉬워하며 자리로 돌아간다."

        "찬미교수..":
            "[player_name]""이 노트로 교수님이 배워야 하는거 아니니.. 찬미교수님?"
            $ chanmi.increase_affection(1)
            c "아 ㅋㅋㅋㅋㅋ 어이없다. 너 진짜 못말려~~ 아잉~~"
            p "찬미는 한층 밝아진 표정으로 자리로 돌아간다."
        
        "별로야":
            "[player_name]""정리가 많이 아쉽네. 다시 해보길 바래"
            $ chanmi.decrease_affection(1)
            c"너 너무한거 아니니!!"
            "찬미는 화난 표정으로 자리로 돌아간다."

    p"[player_name]이(가) 조용히 공부하던 중 아리가 갑자기 어깨를 툭툭 친다"

    a"이 문제 좀 봐줄래..? 나 머리가 잘 안돌아가.."

    menu:
        "문제를 봐준다":
            "아리 옆으로 다가가 문제를 도와준다"
            a"와 너 덕분에 진짜 살았다.. 진짜 고마워!"
            $ ari.increase_affection(1)
            "[player_name]""별거 아니라구 ㅋ"

        "멍청아":
            "[player_name]""넌 머리가 안돌아가는게 아니라. 멍청한거야"
            a"머..뭐라고..?"
            "[player_name]""장난이고 이미 과부화 걸린거야. 좀 쉬면서해"
            "아리가 웃음을 터뜨리며 말한다"
            a"그래 너 정말 태평하다!"
            "아리가 다시 자리로 돌아가 다시 문제를 고민한다"

        "다음에 알려줄게":
            "[player_name]""내 문제도 많이 밀려 있어서.. 나중에 알려줄게!"
            a"내일 모레 시험인데.. 알았어!!"
            $ ari.decrease_affection(1)
            "아리는 다른 사람을 찾아 떠난다."
    "[player_name]""다시 열심히 해볼까?"
    #3hours later
    "[player_name]은(는) 공부를 열심히 하다 잠깐 쉬러 나왔다."
    "[player_name]""어, 세나야 안녕!!"
    p "세나가 인사를 하며 다가왔다."
    s"공부 많이했어?"
    "[player_name]""어.. 나 오늘 하루종일 도서관에 있었다.."
    "[player_name]""지금 잠깐 쉬러 나왔어"
    s "너무 열심히 하는 거 아니야? 좀 쉬면서헤~~ 커피 한 잔 사줄게."
    
    menu:
        "좋은데?":
            "[player_name]""어어 너무 좋다. 가자가자"
            s "좋아, 잠깐 머리 식히는 것도 필요하잖아."
            p "둘은 커피 자판기로 이동하며 대화를 나눈다."
            
            menu:
                "시험 이후 계획에 대해 묻는다":
                    p "시험 끝나면 뭐 할 계획이야?"
                    s3 "나는 무조건 여행 갈 거야. 넌 같이 가볼래?"
                    
                    menu:
                        "농담으로 응답한다":
                            $ affection_s3 += 1
                            p "네가 다 계획했구나. 난 네가 운전만 해주면 따라갈게."
                            s3 "좋아, 넌 그냥 옆에서 초콜릿만 먹고 있어."
                        "진지하게 관심을 보인다":
                            $ affection_s3 += 2
                            p "생각해볼게. 근데 어디로 가려고?"
                            s3 "제주도? 아니면 해외도 좋고. 함께라면 어디든 좋아."  
                            p "학생 3의 열정을 보며 나도 설렜다."

                "최근 스트레스에 대해 이야기한다":
                    p "요즘 스트레스 진짜 많다."
                    s3 "나도 그래. 이번 시험이 끝나면 진짜 쉬고 싶어."
                    
                    menu:
                        "고마워하며 이야기를 이어간다":
                            $ affection_s3 += 2
                            p "너도 힘든데 이렇게 챙겨줘서 고마워."
                            s3 "네가 이렇게 말해주니까 더 힘내야겠다는 생각이 들어."
                        "농담으로 분위기를 바꾼다":
                            $ affection_s3 += 1
                            p "시험 끝나면 우리 둘 다 바로 지쳐 쓰러지겠지?"
                            s3 "넌 멋지게 쓰러질 것 같아. 진짜 웃긴다."
        
        "다음에 쉬자고 한다":
            $ affection_s3 -= 1
            p "지금은 좀 힘들어. 시험 끝나고 같이 놀자."
            s3 "그래, 나중엔 절대 빠지지 마!"
            s3 "그런데, 시험 끝나면 너는 뭐 하고 싶어?"
            
            menu:
                "그냥 푹 쉬고 싶다고 한다":
                    $ affection_s3 += 1
                    p "그냥 푹 쉬고 싶어. 잠도 좀 자고."
                    s3 "네가 푹 쉰다는 건 상상이 안 돼. 넌 쉬다가 더 열심히 할 것 같은데?"
                "아직 정하지 않았다고 한다":
                    $ affection_s3 += 2
                    p "아직 정하지는 않았어."
                    s3 "좋아, 그럼 내 계획에 얹혀. 같이 뭔가 해보자!"
                    p "그거 좋을 것 같아."

        "커피를 사 주겠다고 한다":
            $ affection_s3 += 2
            p "그럼 내가 살게. 너도 열심히 했잖아."
            s3 "역시 넌 너무 착해."
            p "우리는 커피를 마시며 가볍게 이야기를 나눴다."

            s3 "근데 너희 중에서 제일 친하다고 생각하는 사람 있어?"
            
            menu:
                "너라고 답한다":
                    $ affection_s3 += 3
                    s3 "진짜? 그런 줄 몰랐네. 고맙다. 네가 이렇게 말해주니 기분 진짜 좋아진다."
                "모두 친하다고 답한다":
                    $ affection_s3 += 1
                    s3 "그치? 우리 모두가 친한 게 제일 좋은 거 같아."
                "농담으로 넘긴다":
                    $ affection_s3 += 1
                    p "너희 중에 고르라는 건 너무 어려운데?"
                    s3 "알겠어, 그럼 난 첫 번째 후보로 생각할게!"

    p "이렇게 우리는 잠시 휴식을 취하며 다시 공부에 집중할 수 있었다."

    # 커피 자판기 이벤트
    s "너무 열심히 하는 거 아니야? 잠깐 쉬는 것도 좋을 것 같아. 커피 한잔하자."
    
    menu:
        "학생 3의 제안을 받아들인다":
            $ sena.increase_affection(1)
            s "좋아! 잠깐 쉬자."
            p "학생 3과 가벼운 대화를 나누며 긴장이 풀렸다."
            
            menu:
                "학생 3의 고민을 경청하며 조언한다":
                    $ sena.increase_affection(1)
                    s "네가 말해준 덕분에 좀 정리가 된 것 같아. 고마워!"
                "학생 3의 고민을 농담으로 넘긴다":
                    $ sena.increase_affection(1)
                    s "넌 진짜 웃긴다! 덕분에 기분 좋아졌어."
        
        "학생 3의 제안을 거절한다":
            s "알겠어. 그럼 열심히 해봐!"
            p "학생 3은 가볍게 웃으며 혼자 커피를 마시러 갔다."
    
    # 늦은 밤 도서관
    p "늦은 밤이 되어 도서관을 나서려던 순간, 학생 2와 학생 3을 발견했다."
    
    menu:
        "학생 2에게 말을 건다":
            a "아직 안 갔네? 오늘 공부 많이 했어?"
            p "학생 2와 함께 집으로 걸어가며 대화를 나눴다."
            
            menu:
                "학생 2의 고민에 공감하며 들어준다":
                    $ ari.increase_affection(1)
                    a "네가 들어줘서 마음이 한결 편해졌어. 고마워."
                "학생 2의 고민을 대충 넘긴다":
                    a "그럴 수도 있지, 뭐."
                    p "대화가 끊기며 약간의 어색함이 흘렀다."
        
        "학생 3과 나간다":
            s "너도 이제 집 가나? 근처 편의점 들러서 뭐 좀 사갈래?"
            
            menu:
                "학생 3과 편의점에 간다":
                    $ sena.increase_affection(1)
                    s "이 초콜릿 맛있어! 너도 먹어볼래?"
                    p "학생 3과 간단한 간식을 나누며 유대감을 쌓았다."
                "학생 3의 제안을 거절한다":
                    s "그래, 알았어. 그럼 내일 보자!"
                    p "학생 3은 아쉬운 듯 혼자 편의점으로 향했다."
    
    # 엔딩 분기 준비
    p "이렇게 하루가 지나갔다. 앞으로 어떤 관계로 발전하게 될까?"
    
    jump chapter3_end

    return

label chapter3_end:
    $ persistent.chapter3_cleared = True  # 챕터 3 완료 상태 설정
    call screen chapter_select
    return