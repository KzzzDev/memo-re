import axios from "axios";
import {getToken} from "./auth";

const serverAddress = "http://localhost:8000/api/v1"

type Method = "GET" | "POST" | "PUT" | "DELETE"

export const callAPI = async (endPoint: string, method: Method, useAuth: boolean, postData?: object) => {
    console.log("call API")
    const AxiosURL = `${serverAddress}/${endPoint}`
    const Header = useAuth ?
        {
            headers: {
                'accept': 'application/json',
                "Content-Type": "application/json",
                'X-CSRFTOKEN': '2gv6ntkWZTBGBam7Ua97iGPJjYBZI0b1c9VpghPmIWdaXGRssdTXCMQrlD6Bf5Mx',
                "Authorization": `JWT ${getToken()}`
            }
        }
        :
        {
            headers: {
                'accept': 'application/json',
                "Content-Type": "application/json",
                'X-CSRFTOKEN': '2gv6ntkWZTBGBam7Ua97iGPJjYBZI0b1c9VpghPmIWdaXGRssdTXCMQrlD6Bf5Mx',
            }
        }
    let response = ""
    console.log("switch前")
    switch (method) {
        case "GET":
            response =await axios.get(AxiosURL,Header)
            break;
        case "POST":
            console.log("Call Post")
            response = await axios.post(AxiosURL,postData,Header)
            console.log(response)
            break;
        default:
            console.log("xxxxxxxxxxxxxxx")
    }
    console.log("Call後")
    console.log(response)
    return response

}