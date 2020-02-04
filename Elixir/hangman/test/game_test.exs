defmodule GameTest do
  use ExUnit.Case
  doctest Hangman

  alias Hangman.Game

  test "new_game returns structure" do
    game = Game.new_game()
    assert game.turns_left == 7
    assert game.game_state == :initializing
    assert length(game.letters) > 0
    assert game.letters == Enum.map(game.letters, &String.downcase(&1))
  end

  test "state isn't changed for :won or :lost game" do
    for state <- [ :won, :lost ] do
      game = Game.new_game() |> Map.put(:game_state, state)
      assert game = Game.make_move(game, "x")
    end
  end

  test "state isn't changed for :lost game" do
    game = Game.new_game() |> Map.put(:game_state, :lost)
    assert game = Game.make_move(game, "x")
  end

  test "first occurence of letter is not already used" do
    game = Game.new_game()
    game = Game.make_move(game, "x")
    assert game.game_state != :already_used
  end

  test "second occurence of letter is already used" do
    game = Game.new_game()
    game = Game.make_move(game, "x")
    assert game.game_state != :already_used
    game = Game.make_move(game, "x")
    assert game.game_state == :already_used
  end

  test "a good guess is recognized" do
    game = Game.new_game("wibble")
    game = Game.make_move(game, "w")
    assert game.game_state == :good_guess
    assert game.turns_left == 7
  end

  test "a good guess is a won game" do

    game = Game.new_game("wibble")

    #장황한 예시
    # game = Game.make_move(game, "w")
    # assert game.game_state == :good_guess
    # assert game.turns_left == 7
    # game = Game.make_move(game, "i")
    # assert game.game_state == :good_guess
    # assert game.turns_left == 7
    # game = Game.make_move(game, "b")
    # assert game.game_state == :good_guess
    # assert game.turns_left == 7
    # game = Game.make_move(game, "l")
    # assert game.game_state == :good_guess
    # assert game.turns_left == 7
    # game = Game.make_move(game, "e")
    # assert game.game_state == :won
    # assert game.turns_left == 7

    moves = [
      {"w", :good_guess},
      {"i", :good_guess},
      {"b", :good_guess},
      {"l", :good_guess},
      {"e", :won}
    ]

    # 잘못된 테스트 예시
    # game = Game.new_game("wibble")
    # for {guess, state} <- moves do
    #   game = Game.make_move(game, guess) #do 안에서는 매번 새로운 game 객체가 생성된다. 따라서 상태 유지가 되지않음.
    #   assert game.game_state == state
    # end

    # 간략한 예시
    Enum.reduce(
      moves,
      game,
      fn ({ guess, state }, game) ->
        game = Game.make_move(game, guess)
        assert game.game_state == state
        assert game.turns_left == 7
        game
      end
    )

  end

  test "bad guess is recongnized" do
    game = Game.new_game("wibble")
    game = Game.make_move(game, "a")
    assert game.game_state == :bad_guess
    assert game.turns_left == 6
  end

    test "lost game is recognized" do
    game = Game.new_game("w")
    game = Game.make_move(game, "a")
    assert game.game_state == :bad_guess
    assert game.turns_left == 6
    game = Game.make_move(game, "b")
    assert game.game_state == :bad_guess
    assert game.turns_left == 5
    game = Game.make_move(game, "c")
    assert game.game_state == :bad_guess
    assert game.turns_left == 4
    game = Game.make_move(game, "d")
    assert game.game_state == :bad_guess
    assert game.turns_left == 3
    game = Game.make_move(game, "h")
    assert game.game_state == :bad_guess
    assert game.turns_left == 2
    game = Game.make_move(game, "f")
    assert game.game_state == :bad_guess
    assert game.turns_left == 1
    game = Game.make_move(game, "g")
    assert game.game_state == :lost
  end
end
