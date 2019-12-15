#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   battlePokemonPackage.py
@Time    :   2019/12/01 19:23:51
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   将精灵初始信息和对战信息打包成一只对战精灵
'''


class BattlePokemon():
    '''对战精灵的生成'''

    def package_pkmon(self, num, level, name, type1,
                      type2, ability, hp, atk, defend,
                      atk_sp, defend_sp, speed, hp_v, atk_v,
                      defend_v, atk_sp_v, defend_sp_v, speed_v, moves):
        '''
        对战精灵添加
        攻击、防御、速度、特攻、特防、命中率、闪避率
        七项能力等级提高或降低的状态

        '''
        
        statistic = {
            "hp": hp,
            "攻击": atk,
            "防御": defend,
            "特攻": atk_sp,
            "特防": defend_sp,
            "速度": speed
        }
        battle_statistic = {
            "hp": hp,
            "攻击": atk,
            "防御": defend,
            "特攻": atk_sp,
            "特防": defend_sp,
            "速度": speed
        }
        # 宝可梦基本信息
        individual = {
            "hp_v": hp_v,
            "atk_v": atk_v,
            "defend_v": defend_v,
            "atk_sp_v": atk_sp_v,
            "defend_sp_v": defend_sp_v,
            "speed_v": speed_v
        }
        # 宝可梦的状态 濒死，异常，捆绑，混乱
        status_condition = {
            "died": 0,
            "volatile": 0,
            "flinch": 0,
            "confusion": 0,
            "infatuation": 0,
            "storeforce": 0,
            "bound": 0,
            "hardstraight": 0
        }
        # 离场后状态
        base_status = {
            "died": 0,
            "volatile": 0,
        }
        # 能力等级初始值都为0
        statistic_level = {
            "攻击": 0,
            "防御": 0,
            "特攻": 0,
            "特防": 0,
            "速度": 0,
            "命中": 0,
            "闪避": 0
        }
        base_info = {
            "num": num,
            "level": level,
            "name": name,
            "type1": type1,
            "type2": type2,
            "ability": ability,
            "statistic": statistic,
            "individual": individual,
            "status": base_status
            
        }

        battle_info = {
            "battle_statistic": battle_statistic,
            "statistic_level": statistic_level,
            "status": status_condition,
            "moves": moves
        }

        pokemon = {
            "base_info": base_info,
            "battle_info": battle_info,
        }
        return pokemon
