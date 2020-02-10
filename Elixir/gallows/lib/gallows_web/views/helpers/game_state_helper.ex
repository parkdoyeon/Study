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
  # 클라이언트로 이스케이프 없이 문자열을 전송할때 보안이슈가 생기므로 주의해야한다.
  # 가능하면 raw()함수를 통해 전달하거나
  # { :safe, str }형태로 리턴하면 eex파일이 알아서 리스폰스를 처리한다.
  defp alert({ class, message }) do
    """
    <div class="alert alert-#{class}">
      #{message}
    </div>
    """
    |> raw()
  end
end
