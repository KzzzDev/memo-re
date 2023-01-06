const dummyMyBrain = [
    {
        brainId: 1,
        title: "東京に行った",
        keyword: "東京|写真|思い出",
        text_uri: "東京といえば東京タワー！",
        userId: 1,
        ownerId:1,
        image_uri: "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=836&q=80"
    },
    {
        brainId: 2,
        title: "海",
        keyword: "海|夜|思い出",
        text_uri: "夜に見た海",
        userId: 1,
        image_uri: "https://images.unsplash.com/photo-1515405295579-ba7b45403062?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
    },
    {
        brainId: 3,
        title: "育てた花",
        keyword: "花|写真|自然",
        text_uri: "庭に咲いていた花が綺麗だった",
        userId: 1,
        image_uri: "https://images.unsplash.com/photo-1501660034796-9860da6cb741?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
    },
    {
        brainId: 4,
        title: "本屋に行った時の思い出",
        keyword: "本屋|お洒落",
        text_uri: "たまたま入った本屋がとてもお洒落な雰囲気で良かった",
        userId: 1,
        image_uri: "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80"
    },

    {
        brainId: 5,
        title: "NY",
        keyword: "アメリカ|旅行",
        text_uri: "アメリカ旅行でニューヨークに行った時の思い出",
        userId: 2,
        image_uri: "https://images.unsplash.com/photo-1589251204996-3367cc27f084?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2055&q=80",
    },
    {
        brainId: 6,
        title: "ゲレンデで本格的なスキー！",
        keyword: "スキー|旅行",
        text_uri: "本格的な雪山でスキーを楽しんだ",
        userId: 2,
        image_uri: "https://images.unsplash.com/photo-1564869909575-8f55df03ceb1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
    },
    {
        brainId: 7,
        title: "ネコ",
        keyword: "動物|かわいい",
        text_uri: "公園で見つけた猫。",
        userId: 3,
        image_uri: "https://images.unsplash.com/photo-1605214941929-9fd45c986caf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
    }
]

export const getUserBrain = function (id) {
    return dummyMyBrain.filter(brain => brain.userId === id)
}

export const getNoteStatus = function (id) {
    return dummyMyBrain.filter(brain => brain.brainId === id)[0]
}

export const addBrain = function (id){
    const original =         getNoteStatus(id)
    dummyMyBrain.push(

    )
}
console.log(getNoteStatus(1))
