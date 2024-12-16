define p = Character(" ")

label chapter4:
    $ load_game_state()
    $ sync_player_name()

    p "캠퍼스는 축제 준비로 북적이고 있었다. 학과 부스도 점점 모양을 갖춰가고 있다."

    p"[player_name]은 학교에 일찍 도착해 축제 준비를 구경하고 있었다."

    "[player_name]""어? 뭐야 찬미누나 안녕?"
    c"어 [player_name] 일찍왔네 안녕~~"
    "[player_name]""누나 축제부스도 운영했었어? 몰랐네.."
    c "어 맞아맞아 말 안했던가.."
    c"마침 잘왔다 일손이 부족한데 여기좀 도와줄래..?"

    menu:
        "도와준다":
            $ chanmi.increase_affection(5)
            "[player_name]" "당근이지 맏겨만 두라고!"
            c"ㅋㅋㅋㅋㅋㅋㅋ 그래그래 고맙네"
            "[player_name]""그럼 난 뭐를 도와주면 되는데??"
            c"음.. 이리와서 이거 한번만 봐주라"
            c"여기 장식품 좀 더 붙이려 하는데 네가 보기엔 어디에 붙이는 게 더 나을까?"

            menu:
                "중앙에 붙인다":
                    "[player_name]" "중앙에 붙이는게 더 눈에 띄겠지?"
                    c"역시 네 눈썰미는 믿을만해. 좋았어, 그렇게 하자."
            
                "가장자리에 붙인다":
                    "[player_name]""가장자리에 붙이는 게 더 깔끔해 보일 것 같아."
                    c "음, 그렇게 하면 전체적으로 조화롭겠네. 좋은 생각이야."
                
                "장식품이 여기있네..":
                    "[player_name]""어 뭐야 이미 장식품이 부스안에 있는데?"
                    c"어?? 무슨 소리야?"
                    "[player_name]""누나가 장식품 아니냐고 ㅋ"
                    "[player_name]""장식품이 이미 충분해서 안붙여도 되겠는데?"
                    $ chanmi.increase_affection(5)
                    p"찬미의 볼이 붉게 물들었다."
                    c"아니 ㅋㅋㅋ 뭐라는거야"
                    c"그래서 장난치지 말고 어디에 붙일까?"
                    menu:
                        "중앙에 붙인다":
                            "[player_name]" "중앙에 붙이는게 더 눈에 띄겠지?"
                            c"역시 네 눈썰미는 믿을만해. 좋았어, 그렇게 하자."
            
                        "가장자리에 붙인다":
                            "[player_name]""가장자리에 붙이는 게 더 깔끔해 보일 것 같아."
                            c "음, 그렇게 하면 전체적으로 조화롭겠네. 좋은 생각이야."

            "[player_name]" "우리는 장식물을 붙이면서 대화를 이어갔다. 찬미누나 손놀림은 항상 빠르고 정돈되어 있었다."

            c "그런데, 있잖아... 너는 축제 끝나고 뭐 할 계획 있어?"

            menu:
                "뭐 특별한 계획은 없어":
                    "[player_name]" "별다른 계획은 없어. 뭐 쉰다 정도?"
                    c "그럼 나랑 같이 술 마실래? 축제 준비한 사람들끼리 모이는 자리 있는데, 너도 왔으면 좋겠어."
                    "[player_name]""어 근데, 내가 그 자리에 껴도 되는거 맞아??"
                    c"응응! 상관없어 아까 우리 부스 사람들이 너 부르라고 하더라"
                    "[player_name]""그래? 그럼 좋아! 이따 끝나고 연락해!"
                    $ chanmi.increase_affection(5)
                    c"알았어~ 이따 보자"
            
                "혼자 시간을 보내고 싶어":
                    "[player_name]" "아마 혼자 있을 것 같아. 이런 때에 혼자만의 시간도 중요하잖아."
                    c "같이 술 마시자고 하려했는데.. 알았어..."
                    $ chanmi.decrease_affection(5)

        "거절한다":
            $ chanmi.decrease_affection(5)
            "[player_name]""미안, 지금은 좀 어려울 것 같아. 다른 일이 있어서."
            c "아, 알았어. 괜찮아. 내가 조금더 힘내면 되겠지.."

        "도망간다":
            p"[player_name]이(가) 전화를 받는척하며 어딘가로 달려간다"
            c"?"
            $ chanmi.decrease_affection(3)
            "[player_name]""후,, 따돌렸나.. 귀찮게 뭘 도와줘 쯧"

    p"축제가 본격적으로 시작되었다." 
    p"사람들이 하나둘 축재현장으로 모여들기 시작했다."
    
    "[player_name]""와.. 사람들 왜 이렇게 많아.."
    "[player_name]" "나도 한번 본격적으로 축제를 즐겨볼까? 후훗"
    "[player_name]" "바로 소개팅부터 조져야겠다.."
    p"[player_name]은(는) 소개팅부스에 인스타아이디를 적고 돌아왔다."
    "[player_name]" "빨리 연락왔으면 좋겠다~~~ 다른곳도 좀 둘러볼까~"
    "[player_name]은(는) 다른 부스들을 둘러보다가 아리와 마주쳤다"
    a"어 안녕? 너 축제 구경중이었구나?"
    "[player_name]""어어 나도 대학생이니까 한번 경험은 해보고싶었어 ㅎㅎ"
    a "그치, 저기 먹거리 부스 엄청 많던데 같이 돌아볼래?"
    menu:
        "좋아":
            $ ari.increase_affection(5)
            "[player_name]" "좋아! 그럼 뭐 먹어볼래?"
            a "저기 보세요, 핫도그도 있고, 떡볶이도 있고... 음, 난 저 와플이 좀 끌리는데!"
            menu:
                "와플 먹자고 한다":
                    $ ari.increase_affection(5)
                    "[player_name]" "와플 좋아~ 같이 먹자."
                    a"좋아! 나는 딸기 크림 얹은 걸로 할래. 너는?"
                    "[player_name]" "나는 초코 소스 잔뜩 얹은 걸로 할게."
                    a "역시 너도 단 걸 좋아하네! 이렇게 같이 먹으니까 더 맛있는 것 같아."
                    "[player_name]""맛있누~~"
                "떡볶이를 추천한다":
                    "[player_name]" "와플도 좋지만, 떡볶이 한번 먹어볼래? 저기 줄 서 있는 거 보니까 엄청 인기 많아 보여."
                    c "그것도 좋지! 매운 거 잘 먹는 편이야?"
                    "[player_name]" "응, 매운 거 좋아해. 같이 먹으면 더 맛있을 거야."
                    c "그럼 얼른 가자! 네가 추천해준 거니까 더 기대된다."
                "핫도그를 추천한다":
                    "[player_name]" "와플도 좋지만, 핫도그 한번 먹어볼래? 저기 줄 서 있는 거 보니까 엄청 인기 많아 보여."
                    c "그것도 좋지! 나 핫도그 좋아한다룡~"
                    "[player_name]" "아 진짜?? 나도 좋아한다능"
                    c "그럼 얼른 가자! 네가 추천해준 거니까 더 기대된다."
            p"둘은 음식을 맛있게 먹고 서로 할 것을 하러 갔다."


        "거절한다":
            "[player_name]" "미안, 지금은 별로 배가 안 고파서.. (배고픔)"
            c "아, 그래?? 알았어.."
            p"[player_name]은(는) 아리를 버리고 빠르게 도망갔다."
            
    p"혼자 축제를 둘러보던중.."
    "[player_name]""오!! 세나야 안녕 방가방가"
    s"어!!!! 여기서 만나네"
    s"나 마침 하고싶은거 있는데 같이할래??"
    m "같이 회전목마 타러 갈래요? 축제 오면 이런 건 꼭 해야지!"
    menu:
        "좋아":
            $ affection_m += 10
            p "그래, 좋아."
            m "생각보다 너 이런 거 좋아하네. 나랑 있으면 더 재밌어질걸?"
            menu:
                "너랑 있으니까 더 즐거워.":
                    $ affection_m += 5
                    p "응, 너랑 있으니까 더 즐거워."
                    m "진짜? 너 이런 말도 할 줄 아는구나. 생각보다 재밌는 사람이네!"
                "조금 어색하지만 네 덕분에 괜찮아.":
                    p "좀 어색하지만 네가 리드해주니까 괜찮아."
                    m "역시 내가 다 이끌어줘야지! 앞으로도 따라와~"
        "괜찮아":
            p "음, 나는 괜찮아. 네가 다른 친구랑 타는 게 더 좋을 것 같아."
            m "알았어. 아쉬운걸?"


    # 불꽃놀이 (최종 엔딩 결정)
    scene fireworks_night
    with fade

    p "축제의 하이라이트인 불꽃놀이가 시작되었다. 나는 하늘을 올려다보며 생각에 잠겼다."

    if affection_e >= 70:
        e "여기 앉아서 같이 볼래요?"
        p "그래, 그러자."
        e "사실 너랑 있으면 조금 더 나 자신을 믿게 돼. 네가 정말 고마워."
        menu:
            "나도 너랑 함께하고 싶어.":
                p "나도 너랑 더 많은 시간을 보내고 싶어."
                e "정말? 그럼 앞으로도 나와 함께해줄 거지?"
                return
            "우린 친구로 남는 게 좋을 것 같아.":
                p "미안, 그냥 친구로 남는 게 좋을 것 같아."
                e "그렇구나... 그래도 고마워. 좋은 친구가 되어줄게."
                return
    elif affection_m >= 70:
        m "우리 더 가까이 가서 볼까? 너랑 있으면 진짜 좋아."
        menu:
            "나도 네가 좋아.":
                p "나도 네가 좋아. 이런 순간이 계속되면 좋겠어."
                m "역시 나의 센스는 통한다니까! 앞으로도 재밌게 지내자!"
                return
            "우린 친구로 남자.":
                p "미안, 우린 친구로 남는 게 좋을 것 같아."
                m "알겠어. 그래도 너랑 친구로 남아도 행복할 거야."
                return
    elif affection_c >= 70:
        c "조용한 곳에서 같이 볼래요?"
        p "그래, 그게 좋을 것 같아."
        c "너랑 있으니까 모든 게 더 특별해. 나 정말 많이 의지하고 싶어."
        menu:
            "그럴 수 있다면 나도 행복해.":
                p "너랑 같이라면 나도 행복할 것 같아."
                c "정말 고마워. 앞으로 잘 부탁해요."
                return
            "우리 관계는 지금이 좋아.":
                p "우리 관계는 지금이 좋아. 부담 없이 지내고 싶어."
                c "그렇구나... 그래도 고마워. 친구로 남아줘."
                return
    else:
        # 솔로 엔딩
        p "나는 혼자서 불꽃놀이를 보았다. 이번 학기는 나 자신에 대해 많이 배운 시간이었다."
        p "다음번에는 더 나은 내가 될 수 있을 거야. 그리고 그때는, 누군가와 함께일지도 모르지."
        return
    jump chapter4_end

    return

label chapter4_end:
    "플레이 해주셔서 감사합니다!!"
    
    return