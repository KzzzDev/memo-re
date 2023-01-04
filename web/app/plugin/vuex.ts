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
            SelectMode: false,
            SelectedBrainId: []
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

        initShareFlags(state) {
            state.ShareFlags.SelectMode = false
            state.ShareFlags.ShareConfirmMode = false
        },
        // -------------------------------------------------------------------------------------------------------------
        resetSelectBrain(state) {
            state.SelectedBrainId = []
        },
        appendSelectBrain(state, BrainId) {
            let appendList = this.state.SelectedBrainId
            console.log(appendList)

            appendList.push(parseInt(BrainId))
            state.SelectedBrainId = appendList
        },
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
        toggleFriendModalState(context) {
            context.commit("updateFriendModalFlag")
        },
        toggleSearchModalState(context) {
            context.commit("updateSearchModalFlag")
        },
        toggleNoticeModalState(context) {
            context.commit("updateNoticeModalFlag")
        },
        initShareFlags(context) {
            context.commit("initShareFlags")
        },
        toggleSelectMode(context) {
            context.commit("toggleSelectMode")
        },
        offSelectMode(context) {
            context.commit("offSelectMode")
        },
        onShareConfirmMode(context) {
            context.commit("onShareConfirmMode")
        },
        offShareConfirmMode(context) {
            context.commit("offShareConfirmMode")
        },
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