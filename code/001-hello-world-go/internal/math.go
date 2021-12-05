package internal

import (
	"github.com/pkg/errors"
)

func DoMagic(input float64) (float64, error) {
	added := add(input, -2)
	if divided, err := divide(10.0, added); err != nil {
		return 0, errors.Wrap(err, "What the hell dude")
	} else {
		return divided, nil
	}

}

func add(i float64, j float64) float64 {
	return i + j
}

func divide(i float64, j float64) (float64, error) {
	if j == 0 {
		return 0, errors.New("Division by 0")
	}
	return i / j, nil
}
