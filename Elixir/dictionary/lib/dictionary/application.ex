defmodule Dictionary.Application do

  use Application

  def start(_type, _args) do
    Dictionary.Words.start_link()
  end
end
