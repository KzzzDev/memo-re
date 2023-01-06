import {createStore} from "vuex"

const Store = createStore({
    state() {
        return {
            ModalFlags: {
                Friend: false,
                Search: false,
                Notice: false
            },
            ShareFlags: {
                SelectMode: false,
                ShareConfirmMode: false
            },

            SelectedBrainId: [],
            SendUserData:{
                id:"",
                name:"",
                icon:""
            }
        }
    },
    getters: {
        isFriendModalOpen(state) {
            return state.ModalFlags.Friend
        },
        isSearchModalOpen(state) {
            return state.ModalFlags.Search
        },
        isNoticeModalOpen(state) {
            return state.ModalFlags.Notice
        },
        getSelectMode(state) {
            return state.ShareFlags.SelectMode
        },
        getShareConfirmMode(state) {
            return state.ShareFlags.ShareConfirmMode
        },
        getSelectBrain(state) {
            return state.SelectedBrainId
        },
        getSendUserData(state){
            return state.SendUserData
        }
    },
    mutations: {
        // -------------------------------------------------------------------------------------------------------------
        updateFriendModalFlag(state) {
            state.ModalFlags.Friend = !state.ModalFlags.Friend
            state.ModalFlags.Search = false
            state.ModalFlags.Notice = false
        },
        updateSearchModalFlag(state) {
            state.ModalFlags.Friend = false
            state.ModalFlags.Search = !state.ModalFlags.Search
            state.ModalFlags.Notice = false

        },
        updateNoticeModalFlag(state) {
            state.ModalFlags.Friend = false
            state.ModalFlags.Search = false
            state.ModalFlags.Notice = !state.ModalFlags.Notice
        },
        // -------------------------------------------------------------------------------------------------------------
        toggleSelectMode(state) {
            state.ShareFlags.SelectMode = !state.ShareFlags.SelectMode
        },
        offSelectMode(state) {
            state.ShareFlags.SelectMode = false
        },

        onShareConfirmMode(state) {
            state.ShareFlags.SelectMode = false
            state.ShareFlags.ShareConfirmMode = true
        },
        offShareConfirmMode(state) {
            state.ShareFlags.ShareConfirmMode = false
        },
        // /mypageにmount時に呼ばれる。関連するStateを初期化
        initShareFlags(state) {
            state.SelectedBrainId = []
            state.ShareFlags.SelectMode = false
            state.ShareFlags.ShareConfirmMode = false
            state.SendUserData = {
                id:"",
                name:"",
                icon:""
            }
        },
        // -------------------------------------------------------------------------------------------------------------
        setSendUserData(state,userData){
            state.SendUserData = userData
        },
        // -------------------------------------------------------------------------------------------------------------
        // 記憶共有時の画像選択情報を格納するStateの初期化
        resetSelectBrain(state) {
            state.SelectedBrainId = []
        },
        // 画像を追加
        appendSelectBrain(state, BrainId) {
            let appendList = this.state.SelectedBrainId
            console.log(appendList)

            appendList.push(parseInt(BrainId))
            state.SelectedBrainId = appendList
        },
        // 画像を削除
        removeSelectBrain(state, BrainId) {
            let removedList = [];
            removedList.push()
            for (const extractBrainId of state.SelectedBrainId) {
                console.log(extractBrainId)
                // !==にするとextractはint BrainIdはstringとして扱われるので
                if (extractBrainId != BrainId) {
                    removedList.push(parseInt(extractBrainId))
                }
            }
            state.SelectedBrainId = removedList
        }
        // -------------------------------------------------------------------------------------------------------------
    },
    actions: {
        // フレンドモーダルの表示を切り替える処理
        toggleFriendModalState(context) {
            context.commit("updateFriendModalFlag")
        },
        // 検索モーダルの表示を切り替える処理
        toggleSearchModalState(context) {
            context.commit("updateSearchModalFlag")
        },
        // 通知モーダルの表示を切り替える処理
        toggleNoticeModalState(context) {
            context.commit("updateNoticeModalFlag")
        },
        // -------------------------------------------------------------------------------------------------------------
        // 共有に関する情報を全てリセット
        initShareFlags(context) {
            context.commit("initShareFlags")
        },
        // 記憶一覧から共有する記憶を選択する画面に切り替える際に参照するフラグを切り替える処理
        toggleSelectMode(context) {
            context.commit("toggleSelectMode")
        },
        // 記憶選択画面から通常の記憶一覧に戻る歳の処理（これ使ってないかも）
        offSelectMode(context) {
            context.commit("offSelectMode")
        },
        // 記憶選択画面から送信相手の選択画面に移行するためのフラグを切り替える処理
        onShareConfirmMode(context) {
            context.commit("onShareConfirmMode")
        },
        // 送信相手の選択画面を閉じる処理（これも使ってないかもしれない）
        // TODO: 不要な処理は後々精査して整理
        offShareConfirmMode(context) {
            context.commit("offShareConfirmMode")
        },
        // -------------------------------------------------------------------------------------------------------------
        // 共有時の相手側の情報
        setSendUserData(context,userData){
            context.commit("setSendUserData",userData)
        },
        // -------------------------------------------------------------------------------------------------------------
        appendSelectBrain(context, BrainId) {
            context.commit("appendSelectBrain", BrainId)
        },
        removeSelectBrain(context, BrainId) {
            context.commit("removeSelectBrain", BrainId)
        },
        resetSelectBrain(context) {
            context.commit("resetSelectBrain")
        }
    }
})

export default Store