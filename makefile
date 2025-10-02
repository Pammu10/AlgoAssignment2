CXX = g++
CXXFLAGS = -O2 -std=c++17

ALGORITHMS = bubble insertion merge heap quickfirst quickrandom quickmedian radix

all: bin $(ALGORITHMS)

bin:
	mkdir -p bin

$(ALGORITHMS): %: algorithms/%.cpp | bin
	$(CXX) $(CXXFLAGS) $< -o bin/$@

clean:
	rm -f bin/*
