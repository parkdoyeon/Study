defmodule CacheFibo do

  alias CacheFibo.Cache
  defdelegate fib(n), to: Cache, as: :cached_fib

end
