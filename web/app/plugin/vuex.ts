import {createStore} from "vuex"

const Store = createStore({
    state() {
        return {
            ModalFlags: {
                Friend: false,
                Search: false,
                Notice: false
            },
            ShareMode:false
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
        getShareMode(state){
            return state.ShareMode
        }
    },
    mutations: {
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
        updateShareMode(state){
            state.ShareMode = !state.ShareMode
        },
        offShareMode(state){
           state.ShareMode = false
        }
    },
    actions: {
        toggleFriendModalState(context) {
            context.commit("updateFriendModalFlag")
        },
        toggleSearchModalState(context) {
            context.commit("updateSearchModalFlag")
        },
        toggleNoticeModalState(context) {
            context.commit("updateNoticeModalFlag")
        },
        toggleShareMode(context){
            context.commit("updateShareMode")
        },
        offShareMode(context){
            context.commit("offShareMode")
        }
    }
})

export default Store