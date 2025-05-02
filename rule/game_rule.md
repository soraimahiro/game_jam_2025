#  遊戲名稱 的規則  

## 場景  

- 使用迪卡爾座標系 
- 以下兩種場景呈現模式  
    - 線（打小怪時）  
    在這個模式之下，只呈現平行於 x-軸 的數線，於每一個數線上，會有一個「影子」，初始時固定位置，玩家會在其中一個影子處出成。玩家可以左右移動（更改自己的 x-軸 位置），玩家可以上下移動（跳至上下的線上的影子）。  
    - 面（打 Boss 時）  
    在這個模式之下，呈現棋盤狀的座標，「影子」消失，玩家可以直接上下移動。

```py
#player.py
    class player:
        money : int
        hp : int
        skills : skill[]
        pos : vector2
        icon : img
```
```py
#canvas.py
    class canvas:
        state : int # 小怪 Boss 商店 開始畫面、結束畫面、遊戲介紹、Credits
        player : player
        entities : entity[] # 這是一個實體 
        shadows : vector2[] # 座標
        def draw()
        ...
```
- 攻擊  
    - 「玩家會自動定時攻擊」，攻擊技能可選，初始定為向前攻擊。在商店可以購買新技能或購買技能升級。
- 商店  
    - 商店中會有不同技能選擇，可以購買升級。
    - 使用的貨幣來自打死小怪及 Boss
```py
#skill.py
    class skill:
        damage : int
        range : int
        direction : int // mode of moving
```
- 小怪
    - 「小怪會每移動固定步數生在隨機條線的邊上。」而每種小怪會有不同的移動方式（如： 玩家動一格，小怪動一格）「小怪會依照原行動方向行動，既使已掠過玩家。」
    - 如果玩家與小怪碰觸，則受到傷害

- Boss
    - 「Boss 生成在棋的角落。」而每一種 Boss 會有不同的移動和攻擊方式（如：玩家動一格，Boss 向上及右各動一格。攻擊距離為二）「Boss 會一直面朝玩家。」  
```py
#entity.py
    class entity:
        type : int
        pos : vector2
        icon : img
        hp : int
        x_move_amount : int # how long do the entity move
        y_move_amount : int # only boss has this
        wait_time : int # how many rounds do the entity take to move
        round_pass : int # how many rounds pass
        def next_step() # pass to next position
        
```

- 遊戲進行
``` py
#主程式
#game.py
    import pygame
    from file import all_class # 引入所有class

    while 1:
        canvas.draw()
        if 按下方向鍵
            移動玩家
            移動實體 (entity)
            檢查碰撞 (在同一格才算碰撞)

            if 血量為0:
                Lose，結束遊戲
            if 打死 boss:
                Win，結束遊戲(或繼續)
```