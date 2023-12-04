# frozen_string_literal: true

input_string = nil
File.open 'inputs/day04.txt' do |puzzle_in|
  input_string = puzzle_in.read
end

# input_string = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

inputs = input_string.split("\n")
score = 0
task2_score = 0
upcoming_duplicates = [0] * inputs.size
inputs.each do |input|
    winners, mine = input.split(' | ').collect { |numlist| numlist.split(' ') }
    my_winners = mine.intersection(winners)
    # puts upcoming_duplicates.inspect
    num_cards = upcoming_duplicates.shift + 1
    task2_score += num_cards
    next if my_winners.empty?

    card_score = 2 ** (my_winners.size - 1)
    score += card_score
    upcoming_duplicates[...my_winners.size] = upcoming_duplicates[...my_winners.size].collect { |copies| copies + num_cards}
end
puts score
puts task2_score
