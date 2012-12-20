if(!window.console){ window.console = {log:function(){}}; }

$(document).ready(function() {
    var selectedPlayer = 0;
    var selectedTeam = 0;

    var players;
    
    var positions = {
        '2003,04': {
            'offense': [22, 21, 61, 32, 38, 901],
            'defense': [7, 39, 352, 5, 773, 4, 31, 43, 750, 388],
            'midfield': [15, 6, 30, 193, 33, 713, 42, 13, 14, 16, 836],
            'goalie': [1, 2]
        },
        '2005,06': {
            'offense': [22,20,21,23],
            'midfield': [6,16,19,14,17,201,13,837],
            'defense': [10,352,7,8,4,12,5,9,810],
            'goalie': [2,1]
        }
    }
    
    var isMatchActive = function(d) {
        return selectedTeam == d.team_home || selectedTeam == d.team_away;
    }

    function getPosition(player_id, season) {
        for (position in positions[season]) {
            for (var i=0; i < positions[season][position].length; i++) {
                if (positions[season][position][i] == player_id) {
                    return position;
                }
            }
        }
    }

    
    var color = function(d) {
        if (d.goals_home == d.goals_away) {
            return "yellow";
        } else if ((d.home == 1 && d.goals_home > d.goals_away) || (d.home == 0 && d.goals_home < d.goals_away)) {
            return "green";
        } else {
            return "red";
        }
    };
    
    var match_w = 210,
        x = pv.Scale.linear(0,90).range(0, match_w);
    
    /* The root panel. */
    var vis = new pv.Panel()
        .canvas('viz')
        .width(700)
        .height(18*35 + 35)
        .left(10)
        .top(10);

    /* The legend. */
    var legend = new pv.Panel()
        .canvas('legend')
        .width(400)
        .height(300);

    var matches = [];

    vis.add(pv.Label)
        .data(['Phase 1 (Fall)', 'Phase 2 (Spring)'])
        .top(24)
        .font('bold 22px Arvo, Helvetica, Arial, Sans-Serif')
        .left(function() { return (this.index) * 350 + match_w/2 + 15 })
        .textAlign('center')

    vis.add(pv.Panel)
        .data([0,1])
        .left(function() { return this.index*350} )
        .add(pv.Rule)
            .data(pv.range(0,91,45))
            .top(50)
            .font('10px Arvo, Helvetica, Arial, Sans-Serif')
            .strokeStyle('#DDDDDD')
            .left(function(d) { return 15 + x(d) })
            .textAlign('center')
            .visible(function() { return this.index == 1 })
            .add(pv.Label)
            .visible(true)
                .top(50)
                .text(function(d) { return (this.index < 2) ? d : d + 'min'; })
            
    var panels = new pv.Panel();
    vis.add(panels);
    
    panels.add(pv.Panel)
        .data(matches)
        .top(function(d) { return 45 + this.index % 18 * 35; })
        .left(function() { return this.index >= 18 ? 350 : 0; })
        .width(330)
        .height(30)
    
        // 0, 1, 3 points / Logo
        .add(pv.Panel)
            .visible(true)

            // Team logos
            .add(pv.Image) 
                .data(function(d) { return [d.team_home, d.team_away]; })
                .visible(function(d, p) {return isMatchActive(p)})
                .url(function(d, p) { return 'icons/' + d + (!isMatchActive ? 'g' : '') + '.png' })
                .width(20)
                .height(20)
                .bottom(5)
                .left(function(d) { return match_w + 25 + (this.index)*63})

            // Score
            .add(pv.Label) 
                .data(function(d) { return [d.goals_home, ":", d.goals_away]})
                .visible(function(d, p) {return isMatchActive(p)})
                .text(function(d) { return d; })
                .left(function(d) { 
                    if (this.index == 0) return match_w + 62;
                    else return match_w + 53 + (this.index)*9;
                })
                .font('bold 16px Arvo, Helvetica, Arial, Sans-Serif')
                .textAlign(function(d) { return this.index == 0 ? 'right' : 'left'; })
                .textStyle(function(d, p) { return !isMatchActive ? '#CCCCCC' : 'black';
               })
            

            // Points
            .add(pv.Dot)
                .data(function(d) {
                    if (d.goals_home == d.goals_away) {
                        return pv.range(1);
                    } else if ((d.home && d.goals_home > d.goals_away) || (!d.home && d.goals_home < d.goals_away)) {
                        return pv.range(3);
                    } else {
                        return [];
                    }
                })
                .visible(true)
                .shape('circle')
                .size(15)
                .fillStyle(function(d, p) {
                    if (isMatchActive(p)) {
                        return p.home ? "#dbdb8d" : "#ebebca";
                    } else if (selectedTeam || selectedPlayer) {
                        return '#f1f1f1';
                    } else {
                        return p.home ? "#dbdb8d" : "#ebebca";
                    }
                })
                .strokeStyle(null)
                .top(function() { return this.index * 8 + 8; })
                .left(0)

            // hover bar for team selection and home/away indicator
            .add(pv.Bar)
                .data([0,1])
                // .visible(function(d, p) { return (!selectedTeam && !selectedPlayer) } )
                .visible(true)
                .left(15)
                .width(match_w)
                .height(10)
                .top(function(d) { return 5 + 11 * d })
                .strokeStyle('none')
                .fillStyle(function(d, p) {
                    if (selectedTeam && (selectedTeam == p.team_home || selectedTeam == p.team_away)) {
                        return p.home ? "#dbdb8d" : "#ebebca";
                    } else if (selectedTeam || selectedPlayer) {
                        return '#f1f1f1';
                    } else {
                        return p.home ? "#dbdb8d" : "#ebebca";
                    }
                })
            
            // hover bar for player selection
            .add(pv.Bar)
                .data(function(p) { return p.team_home == 1 ? p.players_home : p.players_away; })
                .visible(function(d) { return selectedPlayer == d.id; } )
                .left(function(d) { return 15 + x(d['in']) })
                .width(function(d, p) { 
                    var out = d['out'];
                    for (var i=0; i<p.red_cards.length; i++) {
                        if (p.red_cards[i].player == d.id) {
                            out = p.red_cards[i].minute;
                        }
                    }
                    return x(out - d['in']); 
                } )
                .height(11)
                .top(5)
                .fillStyle("#fedab7")
            
            // cards
            .add(pv.Dot)
                .data(function(p) { 
                    return pv.blend([
    //                    p.yellow_cards.map(function(c) { c.type = "yellow"; return c; }),
                        p.red_cards.map(function(c) { c.type = "red"; return c; })
                    ]); 
                })
                .visible(true)
                .left(function(d) { return 15 + Math.min(match_w, x(d.minute)); })
                .lineWidth(0)
                .fillStyle(function(d, p) { 
                    if (selectedPlayer || selectedTeam) {
                        if (selectedPlayer == d.player || selectedTeam == p.team_home || selectedTeam == p.team_away) return d.type == "red" ? "#c8271f" : "#f6e419"; else return '#DDD'
                    } else return d.type == "red" ? "#c8271f" : "#f6e419";
                })
                .shape("square")
                .top(function(d, p) { 
                    if ((p.home == 0 && p.players_away.reduce(function(l, c) { return l || c.id == d.player}, false)) || (p.home && p.players_home.reduce(function(l, c) { return l || c.id == d.player}, false))) {
                        return 10;
                    } else {
                        return 20
                    }
                })
                .event('mouseover', function(d) { highlightPlayer(d.player)})
                .event('mouseout', function(d) { resetPlayer(d.player)})                
            
            // goals
            .add(pv.Dot)
                .data(function(p) { return p.goals; })
                .left(function(d) { return 15 + Math.min(match_w, x(d.minute)); })
                .fillStyle(function(d, p) { 
                    if (d.Penalty == 1) {
                        return 'white';
                    }
                    if (selectedPlayer || selectedTeam) {
                        if (selectedPlayer == d.player || selectedTeam == p.team_home || selectedTeam == p.team_away) return d.team == 1 ? "#339ebe" : "gray"; else return '#DDD'
                    } else return d.team == 1 ? "#339ebe" : "gray"  
                })
                .strokeStyle(function(d, p) {
                    if (d.Penalty == 1) {
                        if (selectedPlayer || selectedTeam) {
                            if (selectedPlayer == d.player || selectedTeam == p.team_home || selectedTeam == p.team_away) return d.team == 1 ? "#339ebe" : "gray"; else return '#DDD'
                        } else return d.team == 1 ? "#339ebe" : "gray"  
                    } else {
                        return null;
                    }
                })
                .lineWidth(1.5)
                .shape("circle")
                .top(function(d) { return d.team == 1 ? 10 : 21  } )
                .angle(function(d) { return d.team == 1 ? 0 : pv.radians(180)  } )
                .event('mouseover', function(d) { highlightPlayer(d.player)})
                .event('mouseout', function(d) { resetPlayer(d.player)})                
    ;

    function drawVis(matches) {

        // create date
        matches.map(function(d) {
            var strDate = d.date;
            var dateParts = strDate.split(".");

            d.date = new Date(dateParts[2], (dateParts[1] - 1) ,dateParts[0]);
        });

        // sort games by date
        matches.sort(function(a,b) {
            return (a.date.getTime() - b.date.getTime())
        });
        panels.data(matches);
        vis.render();
    }


    var legend_step = 0;
    var windowWidth = document.documentElement.clientWidth;  
    var windowHeight = document.documentElement.clientHeight;   
    var popupHeight = $("#legend").height();  
    var popupWidth = $("#legend").width(); 
    $('#legend').css('top', windowHeight/2-popupHeight/2).css('left', windowWidth/2-popupWidth/2).show();
    
    
    $('#legend a#next').click(function() {
        legendStep(1);
        return false;
    });
    $('#legend a#previous').click(function() {
        legendStep(-1);
        return false;
    });
    $('#legend a#close').click(function() {
        $('#legend').hide();
        return false;
    });
    $('#footer a#showlegend').click(function() {
        legend_step = 7;
        legendStep(0);
        $('#legend').show();
        return false;
    });
    $('#season').change(function() {
        var season = $('#season').val();
        loadPlayerAndTeams(season);
        return false; 
    });


    function legendStep(step) {
        legend_step = legend_step + step;
        legend_step = legend_step % 8;
        $('#legend img').attr('src', 'legend/' + (legend_step + 1) + '.png');
    }


    // Player list
    $('a.player').live({
        mouseover: function() {
           selectedPlayer = $(this).data('id');
           vis.render();
        },
        mouseout: function() {
            selectedPlayer = 0;
            vis.render();
        }
    });
    
    // Player list
    $('a.team').live({
        mouseover: function() {
           selectedTeam = $(this).data('id');
           vis.render();
        },
        mouseout: function() {
            selectedTeam = 0;
            vis.render();
        }
    });
    
    loadPlayerAndTeams('2003,04');
    
    function highlightPlayer(id) {
        $('#playerlist a').each(function() {
             if ($(this).data('id') == id) {
                 $(this).addClass('hover');
             } else {
                 $(this).removeClass('hover');
             }
        });
    }
    
    function resetPlayer(id) {
        $('#playerlist a').each(function() {
             if ($(this).data('id') == id) {
                 $(this).removeClass('hover');
             }
        });
    }
    
    
    function loadPlayerAndTeams(season) {
        $.getScript('data/' + season + '/matches.js');
        console.log(matches);
        
        $('#playerlist ul').empty();
        $.getJSON('./data/' + season + '/players.js', function(data) {
            players = data;
            for (var id in data) {
                player = data[id];
                if (player.team == 1) {
                    var position = getPosition(id, season);
                    var a = $('<a class="player" href="#">' + player.name + '</a>').data('id', id);
                    $('<li></li>').append(a).appendTo('#playerlist #' + position);
                }
            }
        });

    
        $('#teamlist ul').empty();
        $.getJSON('./data/' + season + '/teams.js', function(data) {
            for (var id in data) {
                team = data[id];
                if (id != 1) {
                    var a = $('<a class="team" href="#"><img src="icons/' + id + '.png"/><span class="teamname">' + team + '</span></a>').data('id', id);
                    $('<li></li>').append(a).appendTo('#teamlist ul');
                }
            }
        });
        
        drawVis(matches);
    }

});
