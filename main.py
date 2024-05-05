namespace SpriteKind {
    export const Special = SpriteKind.create()
    export const Portal = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    startGame()
})
function startGame () {
    info.startCountdown(40)
    info.setScore(0)
    scene.setBackgroundImage()
    effects.blizzard.startScreenEffect()
    flower = sprites.create(, SpriteKind.Food)
    rose = sprites.create(, SpriteKind.Food)
    weed = sprites.create(, SpriteKind.Enemy)
    weeds = sprites.create(, SpriteKind.Enemy)
    flower.setPosition(randint(10, 110), randint(10, 110))
    rose.setPosition(randint(10, 110), randint(10, 110))
    weed.setPosition(randint(10, 110), randint(10, 110))
}
function weedPosition () {
    weed.setPosition(randint(10, 110), randint(10, 110))
}
function walk () {
    controller.moveSprite(mySprite)
    if (controller.left.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        500,
        true
        )
    } else if (controller.right.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        500,
        true
        )
    } else if (controller.up.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        500,
        true
        )
    } else {
        animation.runImageAnimation(
        mySprite,
        [],
        500,
        true
        )
    }
}
info.onCountdownEnd(function () {
    pause(200)
    game.setGameOverEffect(true, effects.confetti)
    game.setGameOverMessage(true, "GAME OVER!")
    game.setGameOverScoringType(game.ScoringType.HighScore)
    pause(70000)
    game.reset()
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Food, function (sprite, otherSprite) {
    if (sprite == weed) {
        weedPosition()
    } else if (sprite == weeds) {
        weedsPosition2()
    }
})
info.onScore(10, function () {
    weed.setPosition(randint(10, 110), randint(10, 110))
})
function weedsPosition2 () {
    weeds.setPosition(randint(10, 110), randint(10, 110))
}
function jump () {
    animation.runImageAnimation(
    mySprite,
    [],
    2,
    true
    )
}
function idle () {
    animation.runImageAnimation(
    mySprite,
    [],
    500,
    true
    )
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    if (otherSprite == flower) {
        flower.setPosition(randint(10, 110), randint(10, 110))
        info.changeCountdownBy(0.15)
    } else if (otherSprite == rose) {
        info.changeCountdownBy(0.3)
        info.changeScoreBy(2)
        rose.setPosition(randint(10, 110), randint(10, 110))
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeScoreBy(-1)
    if (otherSprite == weed) {
        weedPosition()
    } else if (otherSprite == weeds) {
        weedsPosition2()
    }
})
let weeds: Sprite = null
let weed: Sprite = null
let rose: Sprite = null
let flower: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundImage()
mySprite = sprites.create(, SpriteKind.Player)
let thresholdLevel = 10
mySprite.startEffect(effects.trail)
mySprite.sayText("Press B to start!")
game.showLongText("Use WASD Keys to move  pick up flowers! Avoid the weeds", DialogLayout.Bottom)
pauseUntil(() => controller.B.isPressed())
mySprite.sayText("")
forever(function () {
    mySprite.setBounceOnWall(true)
    if (controller.anyButton.isPressed() && !(controller.A.isPressed())) {
        walk()
    } else if (controller.A.isPressed()) {
        jump()
        pause(100)
        idle()
    } else {
        idle()
    }
    if (info.score() > thresholdLevel) {
        thresholdLevel += 5
        weedsPosition2()
    }
})
