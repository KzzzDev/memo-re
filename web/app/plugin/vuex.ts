import {createStore} from "vuex"

const Store = createStore({
    state() {
        return {
            ModalFlags: {
                Friend: false,
                Search: false,
                Notice: false
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
    }
})

export default Store