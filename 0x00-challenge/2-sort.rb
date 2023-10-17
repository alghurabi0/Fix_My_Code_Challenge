###
#
#  Sort integer arguments (ascending) 
#
###
result = []

ARGV.each do |arg|
    # Check if the argument is an integer
    if arg =~ /^-?\d+$/
        i_arg = arg.to_i
        is_inserted = false
        i = 0

        # Find the correct position to insert the integer
        while i < result.size do
            if result[i] < i_arg
                i += 1
            else
                result.insert(i, i_arg)
                is_inserted = true
                break
            end
        end

        # If not inserted earlier, append it to the end of the result
        result << i_arg if !is_inserted
    end
end

puts result
