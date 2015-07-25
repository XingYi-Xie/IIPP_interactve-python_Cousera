## Mini-Project的简述与链接
### Week 0 - 注释，字符串，数值，运算符，算术表达式，变量

Mini­project # 0 — “We want... a shrubbery!”

这个mini-­project不是必做的。代码在console输出“We want... a shrubbery!”。它的主要目的是学习在Coursera上交作业和同学之间互评。

模板: http://www.codeskulptor.org/#examples­-shrubbery_template.py
我的解法: http://www.codeskulptor.org/#user40_ZLKjr62Qc3_0.py

此代码没有保存在本repo中。

### Week 1 - 函数，缩进，余数，模块，布尔表达式，逻辑运算符，条件判断语句

Mini­project # 1 — Rock-paper-scissors-lizard-Spock 石头-布-剪刀-蜥蜴-史波克

石头-布-剪刀-蜥蜴-史波克 (RPSLS)是一种有5种选择的石头-剪刀-布的改版 (https://zh.wikipedia.org/wiki/%E7%9F%B3%E5%A4%B4%E3%80%81%E5%89%AA%E5%AD%90%E3%80%81%E5%B8%83%E3%80%81%E8%9C%A5%E8%9C%B4%E3%80%81%E5%8F%B2%E6%B3%A2%E5%85%8B)

在这个mini-project,我们将模拟玩一轮RPSLS的游戏，生成从这些选项中的随机选择，并决定胜利者。结果只是在console输出。

模板: http://www.codeskulptor.org/#examples-rpsls_template.py
name_to_number 测试模板: http://www.codeskulptor.org/#examples-name_to_number_template.py
number_to_name 测试模板: http://www.codeskulptor.org/#examples-number_to_name_template.py

我的解法: http://www.codeskulptor.org/#user40_nVYMNIPJP3_10.py

### Week 2 - Event handlers, 局部变量, 全局变量, SimpleGui模块, 按钮, 输入框

Mini­project # 2 — “Guess the number” game “猜数字”游戏

玩家一（计算机）想一个秘密数，玩家二试着猜出这个数。每次猜数后，玩家一会根据秘密数是高了，低了，还是等于所猜的数，回答，“高一些”，“低一些”或者“正确”。
你将使用输入框和几个按钮与程序进行交互。对于这个project，我们忽略画布，将计算机的回应在console输出。

模板: http://www.codeskulptor.org/#examples-guess_the_number_template.py
测试模板: http://www.codeskulptor.org/#examples-gtn_testing_template.py

我的解法: http://www.codeskulptor.org/#user40_zK8o7hZjMu_1.py

### Week 3 - 画布, 事件驱动的绘图，字符串运算，绘图运算, 计时器

Mini­project # 3 — Stopwatch: The Game 秒表：游戏

这次的 mini-project主要是将在画布上绘制文字与计时器相结合，做一个简单的精确到10分之一秒的数字秒表。这个秒表应该包含"开始","停止","重置"按钮。

模板: http://www.codeskulptor.org/#examples-stopwatch_template.py
format函数的测试模板: http://www.codeskulptor.org/#examples-format_template.py

我的解法: http://www.codeskulptor.org/#user40_FJnCfZCCIy_4.py

### Week 4 - 列表，距离的计算，反射，键盘事件，位置控制，速度控制，可变与不可变的数据

Mini­project # 4 — Pong 乓

这个project我们要做个Pong(乓), 最早的街机游戏之一 (1972). (https://zh.wikipedia.org/wiki/%E4%B9%93) Pong是一个模拟乒乓球的二维运动游戏。两名玩家控制游戏中的乒乓板垂直的在屏幕两边移动。玩家使用乒乓板把球打回去。
我的增加的一个功能：按Space键可暂停游戏。

模板: http://www.codeskulptor.org/#examples-pong_template.py

我的解法: http://www.codeskulptor.org/#user40_sLEgbNF61oTBjTq_3.py

### Week 5 - 鼠标事件，列表方法，iteration and list comprehension, 词典, 载入与绘制图像
Mini­project # 5 — Memory 记忆卡牌游戏

记忆卡牌游戏中，玩家面对一组正面向下的卡牌。一轮就是玩家翻了两张卡牌。如果他们相同，这两张卡牌就一直正面向上。如果两张牌不同，这两张就翻回背面。游戏目标是用最少的次数把所有的卡牌都翻到正面。
我的解法用4 × 4的图像，代替了16 × 1的数字卡片。

模板: http://www.codeskulptor.org/#examples-memory_template.py
记忆卡牌游戏的状态示例: http://www.codeskulptor.org/#examples-memory_states.py

我的解法: http://www.codeskulptor.org/#user40_iXhMGTh3hW_6.py

### Week 6 - 面向对象编程, class fields 与方法, 平铺的图像
Mini­project # 6 — Blackjack 21点

Blackjack（21点）是许多赌场都在玩的简单，流行的纸牌游戏。A可以代表1或11点（玩家选择），K,Q,J代表10点, 其它牌的点数就是他们自身的数值。  一轮Blackjack中, 玩家的目标是达到手上的牌的总点数比庄家大，但不超过21。
我们简化版的游戏规则如下。一开始分别发2张牌给玩家和庄家，庄家其中一纸牌的牌面向下（它的底牌）。玩家可以反复地加牌（hit),请庄家不断给它另一张牌。如果玩家牌的总和超过21, 玩家就爆牌(bust)并输掉这轮。在爆牌之前，玩家可以选择"stand",庄家就会不断地加牌直到它的总数值达到17或更高。 庄家的A必须算做11,除非这会使庄家爆牌。如果庄家爆牌了，玩家羸了。否则玩家和庄家比数牌的大小，总数值大的为赢家。在我们的版本中，数值相同的情况算庄家羸。

模板: http://www.codeskulptor.org/#examples-blackjack_template.py
Card类的测试模板: http://www.codeskulptor.org/#examples-card_template.py
连接列表中的字符串: http://www.codeskulptor.org/#exercises_mouse_join_solution.py
Hand类的测试模板: http://www.codeskulptor.org/#examples-hand_template.py
Deck类的测试模板: http://www.codeskulptor.org/#examples-deck_template.py
Hand类的get_value方法的测试模板: http://www.codeskulptor.org/#examples-getvalue_template.py

我的解法 (基本功能): (secret)
我的解法 (动画效果): (secret)

（不用意思，小U不知道Event handlers， iteration and list comprehension， class fields要怎么翻译）