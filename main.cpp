/*
 * This file is part of Connect4 Game Solver <http://connect4.gamesolver.org>
 * Copyright (C) 2007 Pascal Pons <contact@gamesolver.org>
 *
 * Connect4 Game Solver is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * Connect4 Game Solver is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with Connect4 Game Solver. If not, see <http://www.gnu.org/licenses/>.
 */

#include "solver.hpp"
#include <iostream>
#include <sys/time.h>

using namespace GameSolver::Connect4;

/*
 * Get micro-second precision timestamp
 * uses unix gettimeofday function
 */
unsigned long long getTimeMicrosec() {
  timeval NOW;
  gettimeofday(&NOW, NULL);
  return NOW.tv_sec*1000000LL + NOW.tv_usec;
}

/*
 * Main function.
 * Reads Connect 4 positions, line by line, from standard input
 * and writes one line per position to standard output containing:
 *  - score of the position
 *  - number of nodes explored
 *  - time spent in microsecond to solve the position.
 *
 *  Any invalid position (invalid sequence of move, or already won game)
 *  will generate an error message to standard error and an empty line to standard output.
 */

int solve(Solver &solver, std::string line);

unsigned long long start_time = getTimeMicrosec();

int main(int argc, char** argv) {
	Solver solver;
	if (argc > 1){
		std::string line="";
		std::string null="null";

		if (null.compare(argv[1]) != 0)
			line = argv[1];

		for (int j=1; j<=Position::WIDTH; j++){
			std::cout<<solve(solver, line + std::to_string(j))<<" ";
		}
		std::cout << std::endl;
	}

	exit(0);
}

int solve(Solver &solver, std::string line) {
	Position P;
	int score = 0;
	int result = P.play(line);

	if(result == -1) {//invalid move
		score = 99;
	}else if (result == -2) {//has won already
		score = -99;
	}else {
		score = solver.solve(P, false);
	}

	return score;
}
