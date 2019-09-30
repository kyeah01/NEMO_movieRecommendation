import api from '@/api'
export default {
async searchProfile({ commit }, params) {
    const resp = await api.searchProfile(params)
    const payload = resp.data
    commit('setProfileSearch', payload)
    }
}
