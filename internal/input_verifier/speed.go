package input_verifier

import (
	"errors"
)

const (
	minSpeed float32 = 0.2
	maxSpeed float32 = 2.8
)

func ValidSpeed(speed float32) (float32, error) {
	if speed < minSpeed || speed > maxSpeed {
		return speed, errors.New("speed value should be between 0.2 and 3")
	}
	return speed, nil
}
