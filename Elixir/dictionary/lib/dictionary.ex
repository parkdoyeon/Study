defmodule Dictionary do

  alias Dictionary.Words

  defdelegate random_word(words), to: Words
  defdelegate start(), to: Words, as: :word_list


end
