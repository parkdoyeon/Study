import {Socket} from "phoenix"

export default class HangmanSocket {
    constructor() {
        this.socket = new Socket("/socket", {})
        this.socket.connect()
    }

    connect_to_hangman() {
        this.setup_channel()
        this.channel
            .join() //elixir 함수 호출
            .receive("ok", resp => { //콜백
                console.log("connected: " + resp)
                this.fetch_tally()
            })
            .receive("error", resp => {
                //alert(resp)
                console.log(resp)
                throw(resp)
            })
    }

    setup_channel() {
        //this.socket.channel의 리턴이 함수를 할당한다.
        this.channel = this.socket.channel("hangman:game", {})
        this.channel.on("tally", tally => {
            console.dir(tally)
        })
    }

    fetch_tally() {
        this.channel.push("tally", {})
    }

    make_move(guess) {
        this.channel.push("make_move", guess)
    }

    make_move() {
        this.channel.push("make_move", {})
    }
}