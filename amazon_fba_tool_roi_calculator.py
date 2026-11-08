#!/usr/bin/env python3
"""
AMZScout vs Helium 10 FBA Toolkit ROI & PPC Savings Calculator 2026.
"""
import argparse

def calculate(ad_spend, revenue):
    # Helium 10 Platinum ($948/yr) with estimated 8% PPC ACoS reduction through Cerebro/Magnet optimization
    h10_cost = 948.0
    ppc_savings = ad_spend * 0.08
    net_roi = ppc_savings - h10_cost

    # AMZScout Pro Bundle ($359.99/yr)
    amz_cost = 359.99
    amz_savings = ad_spend * 0.04
    amz_net = amz_savings - amz_cost

    print("=" * 60)
    print("FBA Toolkit ROI Model: AMZScout vs Helium 10")
    print("=" * 60)
    print(f"Annual Gross Revenue:    ${revenue:,.2f}")
    print(f"Annual PPC Ad Spend:     ${ad_spend:,.2f}")
    print(f"Helium 10 Annual Cost:   ${h10_cost:.2f}/year")
    print(f"Helium 10 PPC Savings:   ${ppc_savings:,.2f}/year (8% ACoS trim)")
    print(f"Helium 10 Net Profit ROI:${net_roi:,.2f}/year")
    print("-" * 60)
    print(f"AMZScout Annual Cost:    ${amz_cost:.2f}/year")
    print(f"AMZScout PPC Savings:    ${amz_savings:,.2f}/year (4% ACoS trim)")
    print(f"AMZScout Net Profit ROI: ${amz_net:,.2f}/year")
    print("=" * 60)
    return net_roi

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AMZScout vs Helium 10 Calculator")
    parser.add_argument("--ad-spend", type=float, default=24000.0)
    parser.add_argument("--revenue", type=float, default=120000.0)
    args = parser.parse_args()
    calculate(args.ad_spend, args.revenue)
