defmodule GallowsWeb.HangmanController do
  use GallowsWeb, :controller

  def new_game(conn, _params) do
    render(conn, "new_game.html")
  end

  def create_game(conn, _params) do
    game = Hangman.new_game()
    tally = Hangman.tally(game)

    conn
    |> put_session(:game, game)
    |> render("game_field.html", tally: tally)
  end

  def make_move(conn, params) do
    guess = params["make_move"]["guess"]

    # game = get_session(conn, :game)
    # tally = Hangman.make_move(game, guess)
    # 아래와 같이 정리할 수 있다.
    tally =
      conn
      |> get_session(:game)
      |> Hangman.make_move(guess)

    # input태그에 남는 데이터를 삭제처리해줌
    # (원래는 form전송이 실패할때를 고려하여 요청이 가도 해당 필드를 비워주지 않지만, 우리의 경우 필드값을 남겨줄 필요가 없으므로)
    put_in(conn.params["make_move"]["guess"], "")
    |> render("game_field.html", tally: tally)
  end
end
