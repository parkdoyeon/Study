defmodule Gallows.Views.Helpers.GameStateHelper do
  import Phoenix.HTML, only: [ raw: 1 ]

  @responses %{
    :won => { :success, "You Won!" },
    :lost => { :success, "You Lost!" },
    :good_guess => { :success, "Good Guess!" },
    :bad_guess => { :success, "Bad Guess!" },
    :already_used => { :success, "You already guessed that" },
  }

  def game_state(state) do
    @responses[state]
    |> alert()
  end

  defp alert(nil), do: ""
  defp alert({ class, message }) do
    """
    <div class="alert alert-#{class}">
      #{message}
    </div>
    """
    |> raw()
  end
end
