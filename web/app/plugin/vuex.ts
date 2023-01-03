import {createStore} from "vuex"

const Store = createStore({
    state() {
        return {
            ModalFlags: {
                Friend: false,
                Search: false,
                Notice: false
            },
            ShareMode:false,
            SelectedBrainId:[1]
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
        },
        getSelectBrain(state){
            return state.SelectedBrainId
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
        },
        appendSelectBrain(state,BrainId){
            let appendList = this.state.SelectedBrainId
            console.log(appendList)

           appendList.push(parseInt(BrainId))
            state.SelectedBrainId = appendList
        },
        removeSelectBrain(state,BrainId){
            let removedList = [];
            removedList.push()
            for (const extractBrainId of state.SelectedBrainId){
                console.log(extractBrainId)
                if (extractBrainId != BrainId){
                    removedList.push(parseInt(extractBrainId))
                }
            }
            state.SelectedBrainId = removedList
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
        },
        appendSelectBrain(context,BrainId){
            context.commit("appendSelectBrain",BrainId)
        },
        removeSelectBrain(context,BrainId){
            context.commit("removeSelectBrain",BrainId)
        }
    }
})

export default Store