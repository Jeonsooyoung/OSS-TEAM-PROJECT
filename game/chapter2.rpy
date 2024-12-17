define p = Character(" ")
# define s1 = Character("학생 1")
# define s2 = Character("학생 2")
# define s3 = Character("학생 3")
image bg_beach_day = "background/bg_beach_day.jpg"
image bg_bbq_evening = "background/bbq_evening.jpg"
image bg_drinking_game = "background/drinking.png"
image bg_beach_evening = "background/beach_evening.jpg"
label chapter2:

    $ load_game_state()
    $ sync_player_name()

    scene bg_beach_day
    with dissolve

    play music "audio/CR5_Under_the_Spotlight_FULL_End.ogg" fadein 5.0

    p "새 학기가 시작된 지도 어느덧 한 달. 설렘 가득한 마음으로 컴퓨터공학과 학생들은 MT를 떠나 대천해수욕장에 도착했다."
    p "버스에서 내리자마자, 다들 설렘이 가득한 얼굴로 짐을 정리하고는 하나둘 해수욕장으로 모여들었다."
    p "반짝이는 바다와 시원한 바람이 불고, 모두가 들뜬 목소리로 여기저기서 이야기꽃을 피운다." 

    # 남자 주인공의 독백
    "[player_name]" "바다는 참 오랜만이네. 고등학교 때 수학여행 이후 처음인가"
    "[player_name]" "대학 생활이라... 아직도 실감이 잘 안 나. 이렇게 떠들썩한 분위기 속에 내가 어울릴 수 있을까?"

    # 해수욕장에서의 상황
    s "야, [player_name] 뭐해? 너만 안 와서 다들 기다리고 있잖아! 빨리 와!"
    "[player_name]" "(역시 세나는 여기서도 활발하네..ㅎㅎ)"
    "[player_name]" "알았어. 금방 갈게!"
    p "그렇게 모두가 해수욕장에 모이고, 곧바로 조별로 나누어 게임을 시작했다."
    p "게임은 팀워크를 시험하는 다양한 미션들로 구성되어 있었다. 동기들과 웃고 떠들며 협력하는 모습은 이미 분위기를 한층 뜨겁게 만들었다."
    p "각 조가 경쟁을 벌이면서도, 모두가 즐기고 있다는 것이 느껴졌다."

    p "게임이 한창 진행되던 중, 세나가 [player_name]에게 다가와 말을 걸었다."
    show sena at left with dissolve
    s "야, [player_name]! 다음 게임이 신발 던지기인데 네가 한 번 도전해볼래?"

    menu:
        s "야, [player_name]! 다음 게임이 신발 던지기인데 네가 한 번 도전해볼래?{fast}"
        "내 활약 보고 반해버려도 책임 못 진다?":
            "[player_name]" "훗 드디어 내가 나설 차례인가?"
            "[player_name]" "내가 오송고의 신발 던지기 전설이었지(후후)"
            show sena_happy at left with dissolve
            $ sena.increase_affection(10) # 호감도 상승
            s "ㅋㅋㅋㅋㅋ알겠어, 그러면 부탁해! 우리 팀의 희망은 너야!"
            s "(보기보다 허세가 많네ㅎㅎ)"
            p "[player_name]는 자신감을 내비치며 게임에 도전했다."
            p "주변의 시선이 [player_name]에게 집중되자, 살짝 긴장되는 기운이 감돌았다."
            "[player_name]" "(좋아, 분위기는 내가 다 가져가는 거야. 다들 놀랄 준비는 됐겠지?)"
            "[player_name]" "(신이시여 저에게 힘을 주소서)"
            p "게임이 시작되고, [player_name]는 침착하게 미션을 수행하기 시작했다" 
            p "결과는 대성공! 팀원들은 환호했고, [player_name]도 자신감을 얻었다."
            s "우와! 진짜 잘하는데? 농담인 줄 알았더니 우리 팀 MVP가 여기 있었네!"
            "[player_name]" "흠, 이 정도는 기본이지. 내가 하니까 성공한 거야~!"
            p "주변에서 터져 나오는 박수와 환호 소리에 [player_name]는 살짝 뿌듯한 표정을 지었다."

        "ㅈㄴ 하기 싫은데 어떻게 하지;;":
            "[player_name]" "음… 네가 더 잘할 것 같은데? 내가 하면 팀 점수가 위험할 수도 있으니까..ㅎㅎ"
            $ sena.decrease_affection(10)
            s "야, 설마 나한테 미루는 거야? 한 번 보여줘 봐!!"
            "[player_name]" "(아니 하기 싫다는데 왜 자꾸 시킬려고 하는 거야)"
            "[player_name]" "(좋게 좋게 넘어가 보자)"
            "[player_name]" "아니, 그런 건 아니고... 네가 워낙 잘할 것 같아서 그러지ㅎ~ 우리 팀 에이스는 세나 아니겠어?"
            show sena_sad at left with dissolve
            s "(우리 팀을 위해 한 번쯤 멋지게 나서주는 것도 괜찮았을 텐데... 조금 아쉽네)"
            hide sena_sad with dissolve
            show sena at left with dissolve
            s "치, 쫄보네. 그래, 이 누나가 한 수 보여줄게!"
            p "세나가 자신만만한 표정으로 앞으로 나서자, 팀원들 사이에서 환호와 응원이 쏟아졌다."
            "[player_name]" "세나야, 믿어볼게! 제대로 보여줘!"
            p "게임이 시작되자, 세나는 평생 신발만 던져본 것처럼 자신의 신발을 날리기 시작했다."
            p "[player_name]는 한숨을 쉬며 뒤에서 그 모습을 지켜보았다."
            p "세나가 멋지게 미션을 성공시키자, 모두 박수를 보냈다."
            "[player_name]" "(세나가 잘 해줘서 다행이다)"

    p "각 조가 경쟁을 벌이면서도, 모두가 게임을 즐겼다."
    p "점점 해가 기울어가며 바다는 황금빛으로 물들었고, 모든 팀원들은 숙소로 돌아갔다."
        
    scene bg_bbq_evening
    with fade

    # 바비큐에서의 상황
    p "저녁 시간이 다가오자, 바비큐 준비가 시작되었다."
    p "찬미가 상추, 수저, 포크 같은 것들을 정리하고 있는 모습이 보인다."
    "[player_name]" "(이런 모습, 꽤 보기 좋네... )"
    show chanmi at right with dissolve
    c "야, [player_name], 왜 그렇게 쳐다보고 있어? 내가 그렇게 예쁘냐? ㅋㅋ"
    c "할 일이 없으면 바비큐 준비 좀 도와줘~"

    menu:
        c "할 일이 없으면 바비큐 준비 좀 도와줘~{fast}"
        "예뻐 보이긴 하더라, 도와줄게!":
            "[player_name]" "되게 예쁘던데요ㅎㅎ, 도와줄게요!"
            hide chanmi
            show chanmi_happy at left
            $ chanmi.increase_affection(10)
            c "뭐? 갑자기 그렇게 말하면 좀 부끄럽잖아!"
            p "(찬미는 잠시 머뭇거리며 웃음을 터트린다.)"
            hide chanmi_happy
            show chanmi at right
            c "에이, 말만 그렇게 하지 말고 손부터 움직이시죠!"
            "[player_name]" "넵 알겠습니다!! 뭘 도와주면 될까요?"
            c "고기 좀 준비해 줘. 양념한 거 저기 있어! 고기 구우면서 조심하고, 너무 태우지 말고~"
            "[player_name]" "제가 한때 고기 굽기 장인이었거든요. 제가 돼지고기 소고기로 바꿔드립니다.ㅋㅋ"
            "[player_name]" "(그래도 이렇게 얘기하면서 같이 뭔가 준비하는 게 꽤 즐겁네)"
            p "[player_name](은)는 찬미와 이런저런 이야기를 나누며 고기를 굽기 시작했다."
            p "찬미의 밝은 웃음소리와 함께 바비큐 준비는 한층 더 즐거워졌다"
            
        "음 난 쉬고 싶어요~":
            "[player_name]" "(음... 솔직히 도와주는 건 좀 귀찮은데... 어떻게 말하지?)"
            "[player_name]" "아.. 전 이런 거랑은 좀 안 맞는 스타일이라서."
            p "(장난스러운 표정을 지으며 손을 휘저어 보인다.)"
            hide chanmi
            show chanmi_sad at right
            $ chanmi.decrease_affection(10)
            c "바비큐는 다 같이 준비해야 더 맛있다고!"
            c "정말 안 도와줄 거야~? 그럼 너무 서운한데..."
            "[player_name]" "(이거... 은근히 꼽주네)"
            "[player_name]"  "에이, 알겠어, 알겠어요. 나중에 도와줄게요!"
            "[player_name]"  "대신 지금은 좀 쉬는 시간이라고요~"
            c "휴~ 좋아. 내가 고기 굽다가 지치면 교대 준비하고 있어!"
            "[player_name]"  "알겠어요ㅋㅋ 지치면 얘기해요!"
            "[player_name]"  "(꼭 내가 도와줘야 하는 건 아닌데... 끝까지 날 시키려는 거야? 은근히 고집 있네.)"
            hide chanmi_sad
            show chanmi at right
            p "찬미는 가볍게 한숨을 쉬며 다시 준비를 시작하고, [player_name](은)는 조용히 옆에서 지켜본다."

    hide chanmi

    p "바비큐가 시작되고, [player_name]와 친구들은 고기를 구우며 서로 이야기를 나누었다."
    
    show ari at right
    a "[player_name] 고기 너가 구운거야? 너무 잘 구웠다!!"
    a "[player_name] 보는 것만으로도 군침이 돈다"

    "[player_name]"  "찬미랑 나랑 같이 구웠어! 어때? 흑백요리사에 나가도 될 정도인가?(훗)"
    a "오~ 자신감 넘치는 거 봐? 수고했으니까 특별히 내가 쌈 싸줄게!"

    menu:
        a "오~ 자신감 넘치는 거 봐? 수고했으니까 특별히 내가 쌈 싸줄게!{fast}"
        "아리가 싸준 세상에 하나뿐인 쌈이라니... 이거 아까워서 어떻게 먹어~!":
            "[player_name]" "아리가 싸준 세상에 하나뿐인 쌈이라니... 이거 아까워서 어떻게 먹어ㅠㅠ"
            a "ㅋㅋㅋ 너무 빨진 말고"
            $ ari.increase_affection(10)
            "[player_name]"  "(눈 감으면서 천천히 음미중)"
            "[player_name]"  "아니 뭐야? 아리가 싸줘서 그런건가?"
            "[player_name]"  "나 진짜 거짓말 안치고 살면서 먹었던 쌈중 TOP3 안에 들어"
            hide ari
            show ari_happy at right
            a "TOP3라니ㅋㅋ 말하는 것 봐 나 좀 감동받았는데?!"
            "[player_name]" "진짜야, 농담 아니야. 이거 뭐랄까... 쌈의 균형이 완벽해."
            a "알겠어 알겠어, 그렇게 말해주니 왠지 좀 부끄럽네ㅎㅎ"
            a "(이렇게 말해주면... 설레잖아..)"
            p "아리는 [player_name](이)에게 약간의 설렘을 느낀다"
            hide ari_happy
            show ari at right

        "어... 고맙긴 한데, 내가 직접 싸서 먹을게!":
            "[player_name]"  "고맙긴 한데, 내가 직접 싸서 먹을게"
            "[player_name]"  "좀 부담스러워서..ㅎㅎ"
            hide ari
            show ari_sad at left
            $ ari.decrease_affection(10)
            a "우리 어느 정도 친해진 거 아니었어? 나만 그렇게 생각한 건가.."
            a "부담스러웠다면 미안해.."
            "[player_name]"  "(살짝 얼굴이 붉어지며) 아, 그런 뜻은 아니고... 그냥 내가 부끄러워서.."
            a "부끄러움이 많구나, 그럼 다음부터는 조심할게"
            hide ari_sad
            show ari at right
            "[player_name]"  "(조금 당황한 듯)어.. 조심 안해도 되는데.."
            a "하하.. 알겠어ㅋㅋ 너 생각보다 부끄럼이 많구나? 귀엽네"
            p "아리는 [player_name](이) 부끄러워하는 모습을 보고 귀여움을 느낀다"

    hide ari with fade
    scene bg_drinking_game with fade
    p "바비큐가 마무리되고, 다같이 술을 마시며 게임을 시작했다."
    p "[player_name](이)가 좋아하는 랜덤 게임~ 무슨 게임~ 게임 스타트! "
    p "아파트 아파트 아파트 아파트~~"
    "[player_name]"  "16!"
    "[player_name]"  "오케이~~ 찬미가 걸렸닼ㅋㅋㅋ"
    c "아니니니ㅠㅠㅠㅠ 왜 난데ㅠㅠ"
    s "누!가! 술을 마셔~?!!"
    a "찬미가 술을 마셔 허!(짝짝) 찬!(짝짝) 미!(짝짝) 원샷~ 투샷~"
    c "(꿀꺽 꿀깍) 으악~ 취한다%%"
    s "아니 미친 찬미 죽는다 죽어ㅋㅋㅋ 얘 술찌였네~~"
    s "...? 잠만 얘 헛구역질 하는데"
    c "우웨웨웩"
    a "얘들아 얘 토한다... 어우 나까지 토할 것 같네"
    "[player_name]"  "찬미야 정신좀 차려봐 그러니까 적당히 마시지.."
    p "그렇게 찬미는 30분 동안 화장실에서 고개를 숙인 채 힘겨운 시간을 보냈다"
    c "아.. 얘들아 무슨 일이 이었던 거야.. 머리가 너무 어지럽다.."
    p "그녀의 목소리는 한껏 풀린 기색으로 떨렸고, 눈동자는 초점을 찾지 못한 채 흔들렸다"
    a "괜찮아? 무리하지 말고 조금만 쉬자"
    s "그러는게 좋겠다 찬미야, 정신 좀 차려. 이 상태로 방에 갈 수 있겠어?"
    s "음.. 얘 못갈 것 같은데 [player_name],네가 좀 부축해줘"

    menu:
        s "음.. 얘 못갈 것 같은데 [player_name],네가 좀 부축해줘{fast}"
        "내가 부축해줄게!":
            "[player_name]"  "알겠어. 찬미야, 나한테 기대. 천천히 가자. 방까지는 금방이야"
            $ ari.increase_affection(10)
            $ sena.increase_affection(10)
            $ chanmi.increase_affection(10)
            p "찬미는 조심스럽게 [player_name](이)의 팔에 의지하며 한 걸음씩 앞으로 나아갔다"
            p "찬미의 얼굴은 여전히 창백했지만, 도움에 조금 안도한 것 같았다"
            p "좋아, 거의 다 왔어! 찬미야, 조금만 더 힘내!"
            c "고...고..마워.."
            "[player_name]" "(찬미는 술 취한 모습도 예쁘것 같네...)"
            p "[player_name](은)는 찬미의 비틀거리는 걸음에도 조심스레 발을 맞추며 그녀를 안전하게 데려갔다 "
           

        "너희들이 도와주는 게 나을 것 같아":
            "[player_name]"  "아니야, 내가 부축하는 것보다 너희들이 도와주는 게 나을 것 같아"
            "[player_name]"  "난 조금 뒤에서 도울게"
            $ ari.decrease_affection(10)
            $ sena.decrease_affection(10)
            $ chanmi.decrease_affection(10)
            s "그래? 알겠어... 우리라도 도울게"
            s "(좀 도와주지.. 이 정도도 못 도와주는 거야?)"
            a "그럼 우리가 찬미를 반쯤 부축할게. [player_name], 너는 뒤에서 조심히 지켜봐."
            a "찬미야. 너만 잘 따라와, 알겠지?"
            c "알...겠..어..고마...워.."
            p "그렇게 찬미는 조금 더 안전하게, 셋이 함께 한 발자국씩 나아갔다."
            p "[player_name](은)는 뒤에서 따라오며 지켜보고 있었다."
            s "(허허.. 끝까지 안 도와주네.. 실망이네)"
            a "조금만 더 가면 방이니까 힘내! 우리가 끝까지 도울게!"
            p "찬미는 비틀거리는 걸음에 힘들어 보였지만, 그래도 조금씩 다가갔다."
            "[player_name]"  "(좀 도와줘야 되는 건가.. 아니다 가만히 있자)"
            p "찬미는 겨우 방에 도착해 침대에 누웠다."
            

    s "뭐.. MT오면 이런일도 있는거지ㅋㅋㅋ"
    s "나중에 찬미가 정신 차리면 살짝 놀려볼까ㅎㅎ"
    a "찬미 일어나면 죽었다ㅋㅋㅋ"
    a "(주위를 둘러보며) 근데… 벌써 새벽 3시네. 우리끼리 이제 뭐 하고 놀까?"   
    "[player_name]"  "당연히 술이지! 오늘 밤, 우리 끝까지 가보자고"
    s "역시 술고래는 남달라;; 따라갈 수가 없다니까"
    a "이 누나들이 특별히 같이 마셔줄게!"
    "[player_name]"  "하핫, 누님들 감사합니다! 저 잘 부탁드립니다~"
    p "그렇게 모두가 모여 앉아 왕게임을 시작했다. 웃음소리와 떠드는 소리가 밤하늘에 울려 퍼지며, MT의 마지막 밤은 더욱 활기를 띠었다."
    p "[player_name](은)는 서로 장난치며 웃고 떠드는 친구들 사이에서, 특별한 감정을 느끼며 이 순간을 만끽했다."
    "[player_name]" "(이런 순간이야말로 오래도록 기억에 남겠지… 진짜 MT 오길 잘한 것 같아.)"
    p "그리고 그렇게, 깊은 새벽까지 이어진 그들의 시간은 잊을 수 없는 추억으로 남게 되었다."

    stop music fadeout 5.0


label chapter2_end:
    $ persistent.chapter2_cleared = True  # 챕터 2 완료 상태 설정
    $ save_game_state()
    jump chapter3
    return
