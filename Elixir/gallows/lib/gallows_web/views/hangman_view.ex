defmodule GallowsWeb.HangmanView do
  use GallowsWeb, :view
  import Gallows.Views.Helpers.GameStateHelper

  def game_over?(%{ game_state: game_state }) do
    game_state in [ :won, :lost ]
  end

  def new_game_button(conn) do
    button("New Game", to: "/hangman")
  end

  def turn(left, target) when target >= left do
    "opacity: 1"
  end

  def turn(left, target) do
    "opacity: 0.1"
  end

  def plural_of(word, 1), do: word
  def plural_of(word, _), do: word <> "s"

  def tmp_shopping do
    shopping = [
      { "1 dozen", "eggs" },
      { "1 ripe", "melon" },
      { "4", "apples" },
      { "2 boxes", "tea" },
    ]
    template = """
    quantity | item
    --------------------
    <%= for { q, i } <- list do %>\n
      <%= String.pad_leading q, 8 %> | <%= i %>
    <% end %>
    """
    EEx.eval_string template, [ list: shopping ], trim: true
  end
end
