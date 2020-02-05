defmodule Dictionary do

  alias Dictionary.Words

  defdelegate random_word(), to: Words
  defdelegate start(), to: Words, as: :word_list

end
