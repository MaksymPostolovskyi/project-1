print("---------------------------------------------------------")
print("Проект зробили Ласіца Іван і Постоловський Максим")
print("---------------------------------------------------------")
print("Ласкаво просимо до гри! ")
print("Ви прокинулись в таємничій кімнаті, в кімнаті було 2 дверей ")
choice = input("Виберіть в які двері піти ")

if choice == "1":
    print("---------------------------------------------------------")
    print("Ви пройшли через перші двері ")
    print("В кімнаті були тільки 3 дверей ")
    choice = input("Виберіть в які двері піти ")
    if choice == "1":
        print("---------------------------------------------------------")
        print("Ви пройшли через перші двері ")
        print("Посередині кімнати стояв стіл на якому було таємниче зілля ")
        choice = input("Вз'яти зілля? (так, ні) ")
        if choice == "так":
            print("---------------------------------------------------------")
            print("Ви взяли таємниче зілля ")
            print("Перед вами 2 дверей ")
            choice = input("Виберіть в які двері піти ")
            if choice == "1":
                print("---------------------------------------------------------")
                print("Ви пройшли через перші двері ")
                print("Перед вами опинився ворог ")
                choice = input("Використати зілля? (так, ні) ")
                if choice == "так":
                    print("---------------------------------------------------------")
                    choice = input("Ви витягнули зілля, на кого використати зілля? (себе, ворога) ")
                    if choice == "себе":
                        print("---------------------------------------------------------")
                        print("Ви використали зілля на себе, воно не далі ніякого ефекту ")
                        print("Вас вбив ворог ")
                        print("Кінець гри ")
                        exit()
                    elif choice == "ворога":
                        print("---------------------------------------------------------")
                        print("Ви кинули в ворога зілля ")
                        print("Поки ви чекали ефекту зілля, ворог вас вбив")
                        print("Кінець гри ")
                        exit()
                elif choice == "ні":
                    print("---------------------------------------------------------")
                    print("Ви вирішили битись з ворогом голими руками ")
                    print("В результаті битви ви перемогли ворога але вас було сильно ранено ")
                    print("Ви згадали що у вас лишилось зілля ")
                    choice = input("Використати зілля? (так, ні) ")
                    if choice == "так":
                        print("---------------------------------------------------------")
                        print("Ви використали зілля яке вас сцілило")
                        print("Ви побачили єдині двері в кімнаті ")
                        print("Пройшовши через двері ви побачили вихід із підземелля ")
                        print("Поздоровляю ви вийшли із підземелля ")
                        print("Кінець гри ")
                    elif choice == "ні":
                        print("---------------------------------------------------------")
                        print("Ви побачили єдині двері в кімнаті ")
                        print("Пройшовши через двері ви побачили вихід із підземелля ")
                        print("Але нажаль ви не змогли вийти із підземелля і померли від кровотечі ")
                        print("Кінець гри ")
                        exit()
            elif choice == "2":
                print("---------------------------------------------------------")
                print("Ви пройшли через другі двері ")
                print("Ви вийшли в великій бібліотеці ")
                choice = input("Виберіть в яку сторону бібліотеки піти (ліво, право) ")
                if choice == "ліво":
                    print("---------------------------------------------------------")
                    print("Проходячи між стелажами заповненими книжками вас зацікавила одна книга ")
                    print ("Вз'явзи цю книгу ви прочитали що було написано на ній НЕ ВІДКРИВАТИ ")
                    choice = input("Відкрити книгу (так, ні) ")
                    if choice == "так":
                        print("---------------------------------------------------------")
                        print("Відкривши книгу ви випустили демона закритого в ній ")
                        print("Демон моментально вас вбив ")
                        print("Кінець гри ")
                        exit()
                    elif choice == "ні":
                        print("---------------------------------------------------------")
                        print("Ви поставили книгу на місце і пішли в іншу сторону бібліотеки ")
                        print("По дорозі ви зустріли старого чоловіка який приставився охоронцем бібліотеки ")
                        print("Він дав вам карту підземелля і сказав пошвидше звідси забиратись ")
                        print("Використовуючи карту ви змогли безпечно вийти із підземелля")
                        print("Кінець гри ")
                        exit()
                elif choice == "право":
                    print("---------------------------------------------------------")
                    print("Пройшовши невелику відстань ви зустріли молодого хлопця ")
                    print("Він приставився бібліотекаром і заборонив відкривати деякі книги ")
                    print("Ви попросили його показати як вийти із підземелля ")
                    print("Він запропонував дати карту але взамін потрібно щось віддати ")
                    choice = input("Віддати зілля? (так, ні) ")
                    if choice == "так":
                        print("---------------------------------------------------------")
                        print("Ви віддали зілля ")
                        print("Він сказав що це рідкісне зілля сцілення і дав взамін карту")
                        print("Використовуючи карту ви змогли безпечно вийти із підземелля")
                        print("Кінець гри ")
                        exit()
                    elif choice == "ні":
                        print("---------------------------------------------------------")
                        print("Ви пішли далі і дойшли до дверей ")
                        print("Пройшовши через двері ви побали кімнату з 2 дверями ")
                        choice = input("Виберіть в які двері піти ")
                        if choice == "1":
                            print("---------------------------------------------------------")
                            print("Пройшовши через двері ви побачили вихід із підземелля ")
                            print("Поздоровляю ви вийшли із підземелля ")
                            print("Повернувшись в місто ви змогли продати зілля і розбагатіти")
                            print("Кінець гри ")
                            exit()
                        elif choice == "2":
                            print("---------------------------------------------------------")
                            print("Ви попробували відкрити двері але вони були зачинені ")
                            print("Ви повернулись до перших дверей ")
                            print("Пройшовши через двері ви побачили вихід із підземелля ")
                            print("Поздоровляю ви вийшли із підземелля ")
                            print("Повернувшись в місто ви змогли продати зілля і розбагатіти")
                            print("Кінець гри ")
                            exit()
        elif choice == "ні":
            print("---------------------------------------------------------")
            print("Ви відмовились від таємничого зілля ")
            print("Перед вами 2 дверей ")
            choice = input("Виберіть в які двері піти ")
            if choice == "1":
                print("---------------------------------------------------------")
                print("Перед вами опинився ворог ")               
                print("Ви почали битись з ворогом голими руками ")
                print("В результаті битви ви програли ворогу і померли ")   
                print("Кінець гри ")
                exit()
            elif choice == "2":
                print("---------------------------------------------------------")
                print("Ви пройшли через другі двері ")
                print("Ви вийшли в великій бібліотеці ")
                choice = input("Виберіть в яку сторону бібліотеки піти (ліво, право) ")
                if choice == "ліво":
                    print("---------------------------------------------------------")
                    print("Проходячи між стелажами заповненими книжками вас зацікавила одна книга ")
                    print ("Вз'явзи цю книгу ви прочитали що було написано на ній НЕ ВІДКРИВАТИ ")
                    choice = input("Відкрити книгу (так, ні) ")
                    if choice == "так":
                        print("---------------------------------------------------------")
                        print("Відкривши книгу ви випустили демона закритого в ній ")
                        print("Демон моментально вас вбив ")
                        print("Кінець гри ")
                    elif choice == "ні":
                        print("---------------------------------------------------------")
                        print("Ви поставили книгу на місце і пішли в іншу сторону бібліотеки ")
                        print("По дорозі ви зустріли старого чоловіка який приставився охоронцем бібліотеки ")
                        print("Він дав вам карту підземелля і сказав пошвидше звідси забиратись ")
                        print("Використовуючи карту ви змогли безпечно вийти із підземелля")
                        print("Кінець гри ")
                elif choice == "право":
                    print("---------------------------------------------------------")
                    print("Пройшовши невелику відстань ви зустріли молодого хлопця ")
                    print("Він приставився бібліотекаром і заборонив відкривати деякі книги ")
                    print("Ви попросили його показати як вийти із підземелля ")
                    print("Він запропонував дати карту але взамін потрібно щось віддати ")
                    print("У вас нічого немає ")
                    print("---------------------------------------------------------")
                    print("Ви пішли далі і дойшли до дверей ")
                    print("Пройшовши через двері ви побали кімнату з 2 дверями ")
                    choice = input("Виберіть в які двері піти ")
                    if choice == "1":
                            print("---------------------------------------------------------")
                            print("Пройшовши через двері ви побачили вихід із підземелля ")
                            print("Поздоровляю ви вийшли із підземелля ")
                            print("Кінець гри ")
                            exit()
                    elif choice == "2":
                            print("---------------------------------------------------------")
                            print("Ви попробували відкрити двері але вони були зачинені ")
                            print("Ви повернулись до перших дверей ")
                            print("Пройшовши через двері ви побачили вихід із підземелля ")
                            print("Поздоровляю ви вийшли із підземелля ")
                            print("Кінець гри ")
                            exit()
    elif choice == "2":
        print("---------------------------------------------------------")
        print("Пройшовши через другі двері ") 
        print("Ви побачили 2 дверей і висячий на стіні меч ")
        choice = input("Взяти меч? (так, ні) ") 
        if choice == "так":
            print("---------------------------------------------------------")
            print("Ви взяли меч ")
            choice = input("Виберіть в які двері піти ") 
            if choice == "1":
                print("---------------------------------------------------------") 
                print("Пройшовши через перші двері ви побачили ключ на землі ")
                choice = input("Взяти ключ? (так, ні) ")
                if choice == "так":
                    print("---------------------------------------------------------")
                    print("Ви взяли ключ ")
                    print("Перед вами були тільки 1 двері ")
                    print("Пройшовши через них ви побачили ворога ")
                    choice = input("Використати меч в бою? (так, ні) ")
                    if choice == "так":
                        print("---------------------------------------------------------")
                        print("Ви витягнули меч і ринулись у бій з ворогом ")
                        print("Ви з легкістю перемогли ворога і направились до наступних дверей ")
                        print("Перед вами 2 дверей ")
                        choice = input("Виберіть в які двері піти ")
                        if choice == "1":
                            print("---------------------------------------------------------")
                            print("Двері виявились зачиненими ")
                            choice = input("Використати ключ? (так, ні) ")
                            if choice == "так":
                                print("---------------------------------------------------------")
                                print("Ви відчинили двері ключем")
                                print("Пройшовши через двері ви побали кімнату з 2 дверями ")
                                choice = input("Виберіть в які двері піти ")
                                if choice == "1":
                                   print("---------------------------------------------------------")
                                   print("Ви пройшли через перші двері ")
                                   print("Ви вийшли в великій бібліотеці ")
                                   choice = input("Виберіть в яку сторону бібліотеки піти (ліво, право) ")
                                   if choice == "право":
                                      print("---------------------------------------------------------")
                                      print("Проходячи між стелажами заповненими книжками вас зацікавила одна книга ")
                                      print ("Вз'явзи цю книгу ви прочитали що було написано на ній НЕ ВІДКРИВАТИ ")
                                      choice = input("Відкрити книгу (так, ні) ")
                                      if choice == "так":
                                         print("---------------------------------------------------------")
                                         print("Відкривши книгу ви випустили демона закритого в ній ")
                                         print("Діставши меч ви почали битву з демоном ")
                                         print("В результаті якої ви виграли але були смертельно ранені")
                                         print("Нажаль ніхто не дізнається що ви спасли світ вбивши демона")
                                         print("Кінець гри ")
                                         exit()
                                      elif choice == "ні":
                                           print("---------------------------------------------------------")
                                           print("Ви поставили книгу на місце і пішли в іншу сторону бібліотеки ")
                                           print("По дорозі ви зустріли старого чоловіка який приставився охоронцем бібліотеки ")
                                           print("Він дав вам карту підземелля і сказав пошвидше звідси забиратись ")
                                           print("Використовуючи карту ви змогли безпечно вийти із підземелля")
                                           print("Кінець гри ")
                                           exit()
                                   elif choice == "ліво":
                                        print("---------------------------------------------------------")
                                        print("Пройшовши невелику відстань ви зустріли молодого хлопця ")
                                        print("Він приставився бібліотекаром і заборонив відкривати деякі книги ")
                                        print("Ви попросили його показати як вийти із підземелля ")
                                        print("Він запропонував дати карту але взамін потрібно щось віддати ")
                                        choice = input("Віддати меч? (так, ні) ")
                                        if choice == "так":
                                            print("---------------------------------------------------------")
                                            print("Ви віддали меч ")
                                            print("Він сказав що це непоганий меч і дав взамін карту")
                                            print("Використовуючи карту ви змогли безпечно вийти із підземелля")
                                            print("Кінець гри ")
                                            exit()
                                        elif choice == "ні": 
                                            print("---------------------------------------------------------")
                                            print("Ви пройшли через найдені двері ")
                                            print("Перед вами опинився ворог ")
                                            print("Ви без проблем розправились з ворогом")
                                            print("Перед вами 2 дверей ")
                                            input("Виберіть в які двері піти ")
                                            print("---------------------------------------------------------")
                                            print("Не зважаючи на те які двері ви вибрали ваше чуття вибрало 2 двері")
                                            print("Пройшовши через двері ви побачили вихід із підземелля ")
                                            print("Поздоровляю ви вийшли із підземелля ")
                                            print("Повернувшись в місто ви стали авантюристом і почали досліджувати інші підземелля")
                                            print("Кінець гри ")
                                            exit()
                                            
                                elif choice == "2":
                                   print("---------------------------------------------------------")
                                   print("Пройшовши через двері ви побачили вихід із підземелля ")
                                   print("Поздоровляю ви вийшли із підземелля ")
                                   print("Повернувшись в місто ви стали авантюристом і почали досліджувати підземелля")
                                   print("Кінець гри ")
                                   exit()
                            elif choice == "ні":
                                print("---------------------------------------------------------")
                                print("Ви повернулись до інших дверей")
                                print("Пройшовши через другі двері ви зустріли величезного дракона")   
                                print("Дракон спалив вас")  
                                print("Кінець гри ")
                                exit()
                        elif choice == "2":
                            print("---------------------------------------------------------")      
                            print("Пройшовши через другі двері ви зустріли величезного дракона")   
                            print("Дракон спалив вас")  
                            print("Кінець гри ")   
                            exit() 
                    elif choice == "ні":
                        print("---------------------------------------------------------")
                        print("Перед вами опинився ворог ")               
                        print("Ви почали битись з ворогом голими руками ")
                        print("В результаті битви ви програли ворогу і померли ")   
                        print("Кінець гри ") 
                        exit()          
                elif choice == "ні": 
                    print("---------------------------------------------------------")
                    print("Ви не взяли ключ ")
                    print("Перед вами були тільки 1 двері ")
                    print("Пройшовши через них ви побачили ворога ")
                    choice = input("Використати меч в бою? (так, ні) ")
                    if choice == "так":
                        print("---------------------------------------------------------")
                        print("Ви витягнули меч і ринулись у бій з ворогом ")
                        print("Ви з легкістю перемогли ворога і направились до наступних дверей ")
                        print("Перед вами 2 дверей ")
                        choice = input("Виберіть в які двері піти ")
                        if choice == "1":
                            print("---------------------------------------------------------")
                            print("Двері виявились зачиненими ")
                            print("Ви повернулись до інших дверей")
                            print("Пройшовши через другі двері ви зустріли величезного дракона")   
                            print("Дракон спалив вас")  
                            print("Кінець гри ")
                            exit()
                        elif choice == "2":
                            print("---------------------------------------------------------")      
                            print("Пройшовши через другі двері ви зустріли величезного дракона")   
                            print("Дракон спалив вас")  
                            print("Кінець гри ") 
                            exit()
                    elif choice == "ні":
                        print("---------------------------------------------------------")
                        print("Перед вами опинився ворог ")               
                        print("Ви почали битись з ворогом голими руками ")
                        print("В результаті битви ви програли ворогу і померли ")   
                        print("Кінець гри ")
                        exit()
            elif choice == "2":
                print("---------------------------------------------------------")
                print("Кімната виявилась повністю темна")
                print("Ви почали йти в повній темноті і через декілька кроків почали падати вниз")
                print("Ви впали в яму і розбились")
                print("Кінець гри ")  
                exit()                     
        if choice == "ні":
            print("---------------------------------------------------------")
            print("Ви не взяли меч ")
            choice = input("Виберіть в які двері піти ") 
            if choice == "1":
                print("---------------------------------------------------------") 
                print("Пройшовши через перші двері ви побачили ключ на землі ")
                choice = input("Взяти ключ? (так, ні) ")
                if choice == "так":
                 print("---------------------------------------------------------")
                 print("Ви взяли ключ ")
                 print("Перед вами були тільки 1 двері ")
                 print("Пройшовши через них ви побачили ворога ") 
                 print("Ви почали битись з ворогом голими руками ")
                 print("В результаті битви ви програли ворогу і померли ")   
                 print("Кінець гри ") 
                 exit() 
                if choice == "ні":
                     print("---------------------------------------------------------")
                     print("Ви не взяли ключ ")
                     print("Перед вами були тільки 1 двері ")
                     print("Пройшовши через них ви побачили ворога ") 
                     print("Ви почали битись з ворогом голими руками ")
                     print("В результаті битви ви програли ворогу і померли ")   
                     print("Кінець гри ")
                     exit()    
            elif choice == "2":
                print("---------------------------------------------------------")
                print("Кімната виявилась повністю темна")
                print("Ви почали йти в повній темноті і через декілька кроків почали падати вниз")
                print("Ви впали в яму і розбились")
                print("Кінець гри ")    
                exit()            
    elif choice == "3":
        print("---------------------------------------------------------")  
        print("Пройшовши через треті двері ви попали в скарбницю")
        print("В центрі знаходився п'єдистал на якому була золота корона")
        print("Озирнувшись ви побачи вихід ")
        choice = input("Взяти корону? (так, ні) ")
        if choice == "так":
            print("---------------------------------------------------------")
            print("Ви взяли корону")
            print("Після цього почався землетрус в результаті всі шляхи були завалені камнями")
            print("Ви залишились в скарбниці до смерті")
            print("Кінець гри")
            exit ()  
        if choice == "ні":
            print("---------------------------------------------------------")
            print("Ви вийшли із підземелля")
            print("Кінець гри")
            exit()
if choice == "2":
    print("---------------------------------------------------------")
    print("Коли ви зайшли до кімнати двері зачинились і ви застрягли в кімнаті до смерті")            
    print("Кінець гри")
    exit()
