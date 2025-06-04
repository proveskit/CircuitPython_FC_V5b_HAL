if not contains "tools/uv-0.5.24" $PATH
    # Prepending path in case a system-installed binary needs to be overridden
    set -x PATH "tools/uv-0.5.24" $PATH
end
