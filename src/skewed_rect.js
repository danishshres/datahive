

"use strict"

function _via_draw_rect_skewed(x1, y1, x2, y2, x3, y3){
    _via_reg_ctx.beginPath();
    _via_reg_ctx.moveTo(x1  , y1);
    _via_reg_ctx.lineTo(x2  , y2);
    _via_reg_ctx.lineTo(x3  , y3);
    _via_reg_ctx.lineTo(x1 + x3 - x2  , y1 + y3 - y2);
    _via_reg_ctx.closePath();
  }