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
        isSearchModalOpen(state){
            return state.ModalFlags.Search
        }
    },
    mutations:{
        updateFriendModalFlag(state){
            state.ModalFlags.Friend = !state.ModalFlags.Friend
        }
    },
    actions:{
        toggleFriendModalState(context){
            context.commit("updateFriendModalFlag")
        }
    }
})

export default Store