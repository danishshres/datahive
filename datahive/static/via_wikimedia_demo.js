/*
  VGG Image Annotator (via)
  www.robots.ox.ac.uk/~vgg/software/via/

  Copyright (c) 2016-2018, Abhishek Dutta.
  All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:

  Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
  Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE.
*/

var imageid = 0;

function _via_load_job () {
  // alert("VIA LOAD SUBMODULES")
  lxLoadImg();
}

function lxLoadImg () {
  jQuery.ajax({
    method:  'GET',
    // url:     'http://d.site/via/api.php',
    url: 'http://127.0.0.1:8000/job/',
    // data:    {action: 'get', id: imageid},
    success: function (res) {
      if (!res) {
        return;
      }
      var ants = {};
      if (res.job.file_attributes != ''){
        res.job.file_attributes = JSON.parse(res.job.file_attributes)
      }
      if (res.job.regions != ''){
        res.job.regions =  JSON.parse(res.job.regions)
      }
      ants[res.job.id] = res.job;
      _via_image_id = res.job.id
      import_annotations_from_json(JSON.stringify(ants));
      // import_annotations_from_json(res.job);
      // if (imageid < 1) {
      //   _via_show_img(0);
      //   update_img_fn_list();
      //   _via_settings.ui.image.region_label = 'name';
      //   setTimeout(function () {
      //     lxLoadImg();
      //   });
      // }
      // imageid = +res.ID;
      move_to_next_image();
    },
  });
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function lxPostAndLoadData () {
  jQuery.ajax({
    headers : {
      'X-CSRFToken': getCookie('csrftoken')
    },
    method:  'POST',
    url: 'http://127.0.0.1:8000/job/',
    data:    {
      id:   _via_image_id,
      // data:   JSON.stringify(_via_img_metadata[_via_image_id])
      // filename: _via_img_metadata[_via_image_id]['filename'],
      regions: JSON.stringify(_via_img_metadata[_via_image_id]['regions']),
      file_attributes: JSON.stringify(_via_img_metadata[_via_image_id]['file_attributes']),
    },
    success: function (res) {
      show_message('Annotations saved');
    },
    complete: function(res) {
      lxLoadImg();
      
    }
  });
  
}

window.addEventListener('keydown', function (e) {
  
  if (!_via_is_region_selected
    && (e.target === document.body
      || e.target.id === 'region_canvas')) {
    
    if (e.key === 'ArrowRight' || e.key === 'n') {
      lxPostAndLoadData();
      return;
      // move_to_next_image();
      // e.preventDefault();
    }
    
    // if (e.key === 'ArrowRight' || e.key === 'n') {
    //   lxPostAndLoadData();
    // }
  }
  
}, false);
