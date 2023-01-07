const noteListMaster = [
    {
        noteId: 1,
        title: "東京に行った",
        keyword: "東京,写真,思い出",
        text_uri: "東京といえば東京タワー！",
        userId: 1,
        ownerId: 1,
        image_uri: "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=836&q=80"
    },
    {
        noteId: 2,
        title: "崖から転落中",
        keyword: "絶壁,転がる人,いっしょに転がる熊",
        text_uri: "奇跡的に一命をとりとめた、熊は知らん",
        userId: 1,
        ownerId: 1,
        image_uri: "https://lh3.googleusercontent.com/u/1/drive-viewer/AFDK6gNOzQlIKQ7saEzhteevvd2KiNKUkoMX8UK1oZ_aOlexhKeEt5iXvSFoShm9CV0bpO1bC9-jM-yVzw7PP2rSH7YgWB1TmA=w1642-h766"
    },
    {
        noteId: 3,
        title: "北海道で熊と戦った",
        keyword: "熊,激しい戦い,けがをした男性",
        text_uri: "北海道といえば、ヒグマとの遭遇！",
        userId: 1,
        ownerId: 1,
        image_uri: "https://lh3.googleusercontent.com/u/1/drive-viewer/AFDK6gOpicVJawjnsX2bF3Mm17Axrhs0vxdSibsNTK2_9gv-O9aPGvVpZTUL_iJpIaJS8zjPDR6GZzqlhMwe_n913xMJi3aE=w1642-h762"
    },
    {
        noteId: 4,
        title: "ろうそくの火が消えそうになってる",
        keyword: "家,近くにいる熊,暗い",
        text_uri: "いきなり家が停電、家の外にある電気ブレーカを見に行きたいけど、近くにクマがいるらしい、あかりの代わりにろうそくを使った",
        userId: 1,
        ownerId: 1,
        image_uri: "https://lh3.googleusercontent.com/u/1/drive-viewer/AFDK6gMI4wEvQ3zDA79mg_mQqc1978oHPPls3P7J3x_8llZElypGlvglwxbSlALZqm9y38Vc3IBzEUHWtkUl98lHkaaf3rnT=w1642-h766"
    },
    {
        noteId: 5,
        title: "怒ったクマに追いかけられる男性",
        keyword: "クマ,恐ろしい,男性の人間を追いかける",
        text_uri: "クマに追いかけられた夢をみた",
        userId: 1,
        ownerId: 1,
        image_uri: "https://lh3.googleusercontent.com/u/1/drive-viewer/AFDK6gNPnB_U25QwyRR4uq7t2PJgZDkShWMpS54itJ7h0xO26SvlbBvyLXERIsGHbQ2LphtFgrLmNJVX8ubsBb-9g5zeS3Kt=w1642-h766"
    },
    {
        noteId: 6,
        title: "ずんだ餅を食べた",
        keyword: "ずんだ餅,葉っぱ,美しい",
        text_uri: "とても芸術的なずんだ餅を食べた気がする",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gNqExAlasX8O0a8U2nkWpZjdDQz22SSYevyTGGej573FUhifu8BHUk4EYzcRB5ZYlpTXF7BUJbob0ODac3j8Mn5BX03=w1642-h798"
    },
    {
        noteId: 7,
        title: "おにぎり落とした",
        keyword: "おむすび,落ちる,汚れた",
        text_uri: "あの時落としたおにぎりを再現します。悲しい記憶だった。",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gO1qXlCegLKrXcl_Qv1zJgqP7o4KgVT9bCdp0xHMEDcJhXfs5-_b6xaGdODxAs1dl9FPEGVWB6rFg01lOEA87CxMck_Wg=w1642-h798"
    },
    {
        noteId: 8,
        title: "北海道でカニをいっぱい食べた",
        keyword: "大量のカニを食べる,現実的,机の上",
        text_uri: "カニをたくさん食べたけど、どのくらい食べたのか写真で取り忘れた！よみがえれ！俺の記憶！",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPAhX90MknIFX92tJfaJj1IQslPw0mrv2DU6KhlAwNVF-7qTT31w5abF6SmWpQOIkaiIKywNaq2yPIaiMff4Vqg2N144g=w1245-h798"
    },
    {
        noteId: 9,
        title: "ケーブルが切れた",
        keyword: "イーサネットケーブル,机の上,悲しい",
        text_uri: "長ねんの相棒だったイーサネットケーブルが壊れたのを思い出した。あの時の景色を思い出す。",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gNujijsordQppWWIcOtwyFDLf37mm3tcKx5yoBS6jpVGdhFIqwqzHYbAyfJmWg35OYwiGfqT8hoU69eWDeh2kuQCkJfbA=w1245-h798"
    },
    {
        noteId: 10,
        title: "クマがマッチョすぎる",
        keyword: "クマ,プロレスラー,男性とクマ,レスリング",
        text_uri: "元プロレスラーの俺に勝てるわけねぇ",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gMIJPnMQQMdk0LQtGjWBrPZGpzbFoVweQ45E5ynvp8pAW14ewQ46595ZnuKjjOq3YbCE9CeW7z6up11m_KXPE4XXmeuKA=w1245-h798"
    },
    {
        noteId: 11,
        title: "人の形に見える雲",
        keyword: "青い空,人の形をした雲,幻想的,美しい",
        text_uri: "あの時見た雲の記憶を蘇らせる！！",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPz_790_P9fOY4eHmUSSI1o5nyPaq0slcEtO_aJYGguSZ_3kGurkvlRDRBtMtfxcyFyGDuQHmGKKGl3-3Olzz7MIg_daQ=w1245-h798"
    },
    {
        noteId: 12,
        title: "イケメンな俺！",
        keyword: "イケメン,青年,鏡",
        text_uri: "美で俺に勝てるわけない",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gM1ffGUj9ZNi1kuhBOgvYNgFBJtVYkqd01gPdIiOjF6kJXBls6ogy2qyMNMFwox1arhah3aukHpGEdIeOLMTJDRIvRApg=w1245-h798"
    },
    {
        noteId: 13,
        title: "人の形に見える雲",
        keyword: "青い空,人の形をした雲,幻想的,美しい",
        text_uri: "あの時見た雲の記憶を蘇らせる！！",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPz_790_P9fOY4eHmUSSI1o5nyPaq0slcEtO_aJYGguSZ_3kGurkvlRDRBtMtfxcyFyGDuQHmGKKGl3-3Olzz7MIg_daQ=w1245-h798"
    },
    {
        noteId: 14,
        title: "イケメンな俺！",
        keyword: "イケメン,青年,鏡",
        text_uri: "美で俺に勝てるわけない",
        userId: 2,
        ownerId: 2,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gM1ffGUj9ZNi1kuhBOgvYNgFBJtVYkqd01gPdIiOjF6kJXBls6ogy2qyMNMFwox1arhah3aukHpGEdIeOLMTJDRIvRApg=w1245-h798"
    },
    {
        noteId: 15,
        title: "ボディービルに憧れて",
        keyword: "ボディービルダー,美しい,芸術的,現実的",
        text_uri: "名前も知らないボディービルダーだったけど、脳にこびりついて離れない",
        userId: 3,
        ownerId: 3,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gNk8bIY3ueu5x9k9UTlc9I1FPrHYxJfX338vkQ43R6ojYc9629JTrA52rimK5eExfCHI4_g84gm5vGjfJnNHx_EOb15=w1245-h756"
    },
    {
        noteId: 16,
        title: "マグロの一本釣り",
        keyword: "マグロを釣りあげるボディービルダーの男",
        text_uri: "筋肉もりもりマッチョマンの俺がマグロを一本釣りしても、誰も信じてくれないから記憶に起こしてくれ！",
        userId: 3,
        ownerId: 3,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gMl8ILWsXRxtkTgAqxiX0lsbyef9UL20THGkbvEs6KZhe0GPiDu5m3Rbgb4lv3mWMA51LMaovAwoQinTa7-gZfS5HsyfA=w1245-h756"
    },
    {
        noteId: 17,
        title: "森林伐採前にみた山",
        keyword: "美しい山,秋の季節,美しい紅葉,景色",
        text_uri: "こんなに美しい山が、我々の記憶から失われていく現状をどう思うだろうか？",
        userId: 3,
        ownerId: 3,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gM6NH8tThxwmluif9LAGc--SSc0VZ3kIHq6ecWcLCm8jbcVuLUL8phn-L9Qyopfy9Xo3Ep6zM9kcPFbqkqY9TOC-6nmMg=w1245-h756"
    },
    {
        noteId: 18,
        title: "宇宙人をみた！",
        keyword: "宇宙,宇宙人,不気味",
        text_uri: "宇宙人を見たけど写真を取り忘れました！信じて！",
        userId: 4,
        ownerId: 4,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPSZXA1nFP-85nq9gQLGMJGZvcR52Anai2t7dqDC3cR13o3FxBVsIGhSFSIGvrfqwczzrf0cHuXmDIrahI7g-rohj8EMg=w1245-h756"
    },
    {
        noteId: 19,
        title: "お皿が割れた悲しい",
        keyword: "破壊されたお皿",
        text_uri: "お気に入りのお皿が割れて悲しかった。最後の姿を残したい。",
        userId: 4,
        ownerId: 4,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gMzA1izMPsFOAnlYwklNJc80mANHxDe95o2tvCUZiWH47qBANbI2EGktPDC14h2lmm026uvZzvg6m9zMVkqqA_YjKpi=w1245-h756"
    },
    {
        noteId: 20,
        title: "危機一髪",
        keyword: "衝突事故,車から逃げる人",
        text_uri: "車にぶつかりそうだったけどギリギリ避けて助かった",
        userId: 4,
        ownerId: 4,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gMnnHMhXQr1WpB3mniELpPofupqHV5PBmBtcas0GhlWj5bxBs6BdKRvqtRFt-R50xD_a3C1FN-BxP3qBUFzHdf_s57E=w1245-h756"
    },
    {
        noteId: 21,
        title: "でかい鶏",
        keyword: "人間よりでかい,巨大な鶏,鶏が見下ろす",
        text_uri: "実際そんな鶏を見たことはないけど、幼かった頃に鶏にいじめられたため、鶏にトラウマを持っています。",
        userId: 4,
        ownerId: 4,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gMicD-2V0Uw8Ai4Ni2GvL4CYUPFexAei2G1i2TZfHSg0G4UKemlhfmpLiATpLyioVVQatBz1RzAIjgsXNDx0Rf0hBYWXw=w1245-h756"
    },
    {
        noteId: 22,
        title: "海の魚たち",
        keyword: "美しい海,魚,たくさんの魚",
        text_uri: "きれいな海でたくさんのお魚さんたちと戯れました！楽しかったです！",
        userId: 4,
        ownerId: 4,
        image_uri: "https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gNTBXfbdd0Ub6UH5iWG6XfLqJ6fAZ_71gmdgsWqn4PohjwVlIs6Tp85wG9V85QTAdy-XBtLKdQeRx8fx9nSKSePfXnGHQ=w1245-h756"
    }
]

const userListMaster = [
    {
        userId: 1,
        name: "ずんだもん",
        icon: "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80",
        userTag: ["おんなのこ？ ", "ボイスロイド"]
    },
    {
        userId: 2,
        name: "A子",
        icon: "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80",
        userTag: ["おんなのこ ", "ボイスロイド"]
    },
    {
        userId: 3,
        name: "B男",
        icon: "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80",
        userTag: ["おとこのこ ", "ボイスロイド"]
    },
    {
        userId: 4,
        name: "職人X",
        icon: "https://images.unsplash.com/photo-1502680390469-be75c86b636f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8JUU4JTgxJUI3JUU0JUJBJUJBJTIwJUUzJTgyJUI1JUUzJTgzJUJDJUUzJTgzJTk1JUUzJTgyJUEzJUUzJTgzJUIzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        userTag: ["職人", "伝統工芸", "サーフィン"]
    },
]


const friendListMaster = {
    "user1": [
        2,
        3,
        4
    ],
    "user2": [
        1,
        3
    ],
    "user3": [
        1,
        2
    ],
    "user4": [
        1
    ]
}

export const insertNoteData = function (noteData) {
    let noteList = JSON.parse(localStorage.getItem("noteList"))
    if (!noteList) {
        noteList = noteListMaster
    }
    noteList.push(noteData)
    localStorage.setItem("noteList", JSON.stringify(noteList))

}

export const getFriendList = function (id) {
    let friendList = JSON.parse(localStorage.getItem("friendList"))
    if (!friendList) {
        friendList = friendListMaster
    }
    if (!friendList.hasOwnProperty("user" + id)) {
        return []
    }
    const ResultList = []
    for (const MyFriendId of friendList[`user${id}`]) {
        console.log(MyFriendId)
        ResultList.push(getUserData(MyFriendId))
    }
    return ResultList
}


export const getUserData = function (id) {
    let userList = JSON.parse(localStorage.getItem("userList"))
    if (!userList) {
        userList = userListMaster
        localStorage.setItem("userList", JSON.stringify(userListMaster))
    }
    return userList.filter(user => user.userId === id)[0]
}

export const getUserBrain = function (id) {
    let noteList = JSON.parse(localStorage.getItem("noteList"))
    if (!noteList) {
        noteList = noteListMaster
        localStorage.setItem("noteList", JSON.stringify(noteListMaster))
    }
    return noteList.filter(brain => brain.userId === id)
}

export const getNoteStatus = function (id) {
    let noteList = JSON.parse(localStorage.getItem("noteList"))
    if (!noteList) {
        noteList = noteListMaster
        localStorage.setItem("noteList", JSON.stringify(noteListMaster))
    }
    return noteList.filter(note => note.noteId === id)[0]
}

export const shareNote = function (noteId, userId) {

    const target = getNoteStatus(noteId)
    console.log(target)
    target.userId = userId
    target.noteId = getNextId()
    console.log(target)
    let noteList = JSON.parse(localStorage.getItem("noteList"))
    if (!noteList) {
        noteList = noteListMaster
    }
    noteList.push(target)
    localStorage.setItem("noteList", JSON.stringify(noteList))
}

// 死ぬほど雑なコード
export const getNextId = function () {
    let noteList = JSON.parse(localStorage.getItem("noteList"))
    if (!noteList) {
        noteList = noteListMaster
        localStorage.setItem("noteList", JSON.stringify(noteListMaster))
    }
    let MAX_ID = -1
    for (const note of noteList) {
        if (MAX_ID < note.noteId) {
            MAX_ID = note.noteId
        }
    }
    return MAX_ID + 1
}