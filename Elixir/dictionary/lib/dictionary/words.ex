defmodule Dictionary.Words do

  def random_word(words) do
    words
    |> Enum.random()
  end

  def word_list() do
    "../../assets/words.txt"
    |> Path.expand(__DIR__)
    |> File.read!()
    |> String.split(~r/\n/)
  end
end
