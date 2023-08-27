import React from "react";

function Rating({ value, text, color }) {
  const starDisplay = (count) => {
    return (
      <i
        style={{ color }}
        className={
          value >= count
            ? "fas fa-star"
            : value >= count + 0.5
            ? "fas fa-star-half-alt"
            : "far fa-star"
        }
      ></i>
    );
  };

  return (
    <div className="rating">
      <span>{starDisplay(1)}</span>
      <span>{starDisplay(2)}</span>
      <span>{starDisplay(3)}</span>
      <span>{starDisplay(4)}</span>
      <span>{starDisplay(5)}</span>

      <div>{text && text}</div>
    </div>
  );
}

export default Rating;
